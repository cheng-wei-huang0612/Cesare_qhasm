#!/usr/bin/env python3
"""
This script performs the following steps (for NTT_4 usage):
1. Generate a list of prime moduli P (size = num_of_moduli).
2. For each modulus p in P, find a "4th root of unity" if p-1 multiple of 2048 
   (這裡程式名稱為 primitive_4th_root_of_unity，但實際就是 primitive root^((p-1)/2048)).
3. Generate required NTT-related arrays (omegas, mu_omegas) in bit-reversed order (2D).
4. Generate random polynomials f, g (small demonstration, using normal distribution).
5. Flatten the 2D arrays into 1D arrays for omegas, mu_omegas, 
   and also compute inverses_of_two[].
6. Write all generated data into:
   - data.py (純 Python),
   - data.h / data.c (C header & definition).
"""

import math
import numpy as np

# ----------------------------------------------------------------------------
# Global parameters
# ----------------------------------------------------------------------------
logn_top      = 2      # total size = 2^10 = 1024 (example)
n_small       = 1 << 2  # for demonstration, we do small polynomial length=4
bit_length    = 27      # we want prime moduli around 2^27
num_of_moduli = 4       # we only need 4 primes for NTT_4
num_of_test   = 10      # not used in sample code, but you can expand

# ----------------------------------------------------------------------------
# Step 1: Generate prime moduli
# ----------------------------------------------------------------------------

def mk_primetest():
    """
    Generate a prime sieve up to max_p=65536, and return a list of primes.
    We'll use it to test primality of ~2^27 scale numbers, 
    though it's only partial (trial division up to 65536).
    """
    max_p = 65536
    max_q = 256  # sqrt(65536) = 256
    tab = [True]*max_p
    tab[0] = False
    tab[1] = False
    for i in range(2, max_q):
        if tab[i]:
            for j in range(i*2, max_p, i):
                tab[j] = False
    primelist = []
    for i in range(2, max_p):
        if tab[i]:
            primelist.append(i)
    return primelist

def is_prime(p, primelist):
    """
    Test primality by trial dividing using primes up to sqrt(p).
    p < 2 => not prime
    If p even => not prime
    Then trial divide by primes in primelist.
    """
    if p < 2:
        return p == 2
    if (p & 1) == 0:   # even
        return False
    for r in primelist:
        if r*r > p:
            return True
        if (p % r) == 0:
            return False
    return True

def mk_moduli(bit_len=31, wanted=4):
    """
    Starting from 2^bit_len - 2047, keep subtracting 2048 
    and pick the prime p if is_prime(p).
    Collect 'wanted' primes in descending order.
    """
    primelist = mk_primetest()
    moduli = []
    startp = (1 << bit_len) - 2047
    p = startp
    while len(moduli) < wanted:
        if is_prime(p, primelist):
            moduli.append(p)
        p -= 2048
    return moduli

# ----------------------------------------------------------------------------
# Step 2: Find 4th root of unity (really we want 2048-th root) 
# ----------------------------------------------------------------------------

def prime_factors(n):
    """Return prime factors (not unique)."""
    facts = []
    d = 2
    while d*d <= n:
        while n % d == 0:
            facts.append(d)
            n //= d
        d += 1 if d==2 else 2
    if n>1:
        facts.append(n)
    return facts

def is_primitive_root(g, p, pfactors):
    """Check if g is a primitive root mod p, given prime factors of p-1."""
    order = p - 1
    for f in set(pfactors):
        if pow(g, order // f, p) == 1:
            return False
    return True

def find_primitive_root(p):
    """Find a primitive root mod p."""
    pfactors = prime_factors(p-1)
    for g in range(2, p):
        if is_primitive_root(g, p, pfactors):
            return g
    return None

def primitive_2048th_root_of_unity(p):
    """
    We want g^((p-1)/2048) mod p if (p-1)%2048==0.
    If not divisible => return 0 to indicate no 2048-th root found.
    """
    if (p-1)%2048 != 0:
        return 0
    g = find_primitive_root(p)
    if g is None:
        return 0
    e = (p-1)//2048
    return pow(g, e, p)

# ----------------------------------------------------------------------------
# Step 3: Flattening, bitreverse, Barrett
# ----------------------------------------------------------------------------

def bitrev(x, bits):
    """Bit-reverse of x in 'bits' length."""
    r=0
    for i in range(bits):
        r = (r<<1)| (x&1)
        x >>=1
    return r

def int32(x):
    """
    Force x into 32-bit signed range, two's complement style.
    In Python, integers are unbounded, so we manually mask and sign-extend.
    """
    x &= 0xFFFFFFFF  # keep lower 32 bits
    # convert to signed
    if x & (1 << 31):
        x -= (1 << 32)
    return x

def Mu(b, N):
    """
    Compute mu = round( bR / 2N )
    """
    # Just do a normal Python integer division for the main ratio, but wrap afterwards:
    base_approx = round((b * (2**32)) / (2 * N))  
    mu = int32(base_approx)
    if mu != base_approx:
        print(f"Warning: mu={mu} is not equal to the rounded value {base_approx}<--------------------------------------")
    return mu


def omegas_gen(omega, n, p, logn):
    """
    Return array of length 'n', with bit-reversed index storing 
    successive powers of 'omega' mod p.
    """
    w = 1
    arr = [0]*n
    for i in range(n):
        br = bitrev(i, logn)
        arr[br] = w
        w = (w*omega) % p
    return arr

def mu_omegas_gen(omegas, p):
    """
    Return an array of same length as 'omegas', each element = Mu(omegas[i],p).
    """
    return [ Mu(x, p) for x in omegas ]

def compute_inverses_of_two(primes):
    """Compute modular inverse of 2 for each prime in 'primes'."""
    invs = []
    for pp in primes:
        invs.append(pow(2, -1, pp))
    return invs

# ----------------------------------------------------------------------------
# Step 4: polynomials f, g (demo usage)
# ----------------------------------------------------------------------------

def prng(sigma):
    """
    Return an integer ~ gaussian(0, sigma).
    Here we do int(abs(normal(0,sigma))).
    """
    return int(abs(np.random.normal(0,sigma,1)[0]))

def Falcon_poly_generator(n, q=12289):
    """
    sample polynomial length n, ~ normal(0,sigma).
    sigma ~ sqrt(q/(2n)) * 1.17
    """
    sigma = math.sqrt(q/(2*n)) * 1.17
    pol = []
    for i in range(n):
        pol.append(prng(sigma))
    return pol

def mod_mul_standard(a, b, p):
    result = (a * b) % p
    if result > (p>>1):
        result -= p
    return result
# ----------------------------------------------------------------------------
# Main Code
# ----------------------------------------------------------------------------

if __name__ == "__main__":

    # 1) build prime moduli
    P = mk_moduli(bit_length, num_of_moduli)
    assert len(P) == num_of_moduli

    # 2) compute each prime's 2048-th root
    omega_2048 = [ primitive_2048th_root_of_unity(p) for p in P ]
    
    for i in range(num_of_moduli):
        prod = omega_2048[i]
        for j in range(11-1):
            prod = mod_mul_standard(prod, prod, P[i])
        assert prod == -1

    # 3) compute inverses of 2
    inverses_of_two = compute_inverses_of_two(P)

    # 4) generate polynomials f,g (just small length n_small=4 for demonstration)
    a0_poly = Falcon_poly_generator(n_small)
    a1_poly = Falcon_poly_generator(n_small)
    a2_poly = Falcon_poly_generator(n_small)
    a3_poly = Falcon_poly_generator(n_small)

    b0_poly = Falcon_poly_generator(n_small)
    b1_poly = Falcon_poly_generator(n_small)
    b2_poly = Falcon_poly_generator(n_small)
    b3_poly = Falcon_poly_generator(n_small)
    # 5) generate 2D array of (omegas[i], mu_omegas[i]) for each prime p
    n = (1<<logn_top)   # e.g. 1024
    # disclaim: we only do 2048-th if p-1 divisible by 2048 => else we get zero
    # for demonstration, partial usage
    def MODmul(a,b,mod):
        return ((a%mod)*(b%mod))%mod

    all_omegas = []
    all_mu_omegas = []
    for i, p in enumerate(P):
        w = omega_2048[i]
        if w==0:
            # no 2048-th root => create dummy
            arr_omegas = [1]*n
            arr_mu     = [1]*n
        else:
            arr_omegas = omegas_gen(w,n,p,logn_top)
            arr_mu     = mu_omegas_gen(arr_omegas,p)
        all_omegas.append(arr_omegas)
        all_mu_omegas.append(arr_mu)

    # flatten arrays
    flat_omegas = []
    flat_mu_omegas = []
    for i in range(num_of_moduli):
        flat_omegas.extend(all_omegas[i])
        flat_mu_omegas.extend(all_mu_omegas[i])

    # ----------------------------------------------------------------------------
    # Write to data.py
    # ----------------------------------------------------------------------------
    with open("data.py","w") as fp:
        fp.write("# This file was generated by ntt_4 data generator.\n\n")
        fp.write(f"logn_top = {logn_top}\n")
        # P
        fp.write("P = [")
        for idx, val in enumerate(P):
            fp.write(f"{val}, ")
        fp.write("]\n\n")

        # omega_2048
        fp.write("omega_2048 = [")
        for idx, val in enumerate(omega_2048):
            fp.write(f"{val}, ")
        fp.write("]\n\n")

        # Flatten omegas
        fp.write("# Flattened 2D omegas\n")
        fp.write(f"omegas = [")
        for val in flat_omegas:
            fp.write(f"{val}, ")
        fp.write("]\n\n")

        fp.write("# Flattened 2D mu_omegas\n")
        fp.write("mu_omegas = [")
        for val in flat_mu_omegas:
            fp.write(f"{val}, ")
        fp.write("]\n\n")

        # inverses_of_two
        fp.write("# inverses of 2 modulo each prime\n")
        fp.write("inverses_of_two = [")
        for val in inverses_of_two:
            fp.write(f"{val}, ")
        fp.write("]\n\n")

        # 假設我們已有這 8 個多項式
        # a0_poly, a1_poly, a2_poly, a3_poly, b0_poly, b1_poly, b2_poly, b3_poly = ...

        polynomial_list = [
            ("a0", a0_poly),
            ("a1", a1_poly),
            ("a2", a2_poly),
            ("a3", a3_poly),
            ("b0", b0_poly),
            ("b1", b1_poly),
            ("b2", b2_poly),
            ("b3", b3_poly),
        ]



        for (name, poly) in polynomial_list:
            fp.write(f"{name} = [")
            for val in poly:
                fp.write(f"{val}, ")
            fp.write("]\n\n")   # each polynomial ends with a blank line



    # ----------------------------------------------------------------------------
    # Write data.h / data.c (C version)
    # ----------------------------------------------------------------------------
    elems_per_line = 10
    with open("data.h","w") as fh:
        fh.write("#ifndef DATA_H\n")
        fh.write("#define DATA_H\n\n")
        fh.write("#include <stdint.h>\n\n")
        fh.write("extern const int logn_top;\n\n")

        fh.write(f"extern const uint32_t P[{len(P)}];\n")
        fh.write(f"extern const uint32_t omega_2048[{len(omega_2048)}];\n")
        fh.write(f"extern const uint32_t omegas[{len(flat_omegas)}];\n")
        fh.write(f"extern const uint32_t mu_omegas[{len(flat_mu_omegas)}];\n")
        fh.write(f"extern const uint32_t inverses_of_two[{len(inverses_of_two)}];\n\n")



        for (name, poly) in polynomial_list:
            fh.write(f"extern const int32_t {name}[{len(poly)}];\n")


        fh.write("\n#endif // DATA_H\n")

    with open("data.c","w") as fc:
        fc.write('#include "data.h"\n\n')
        fc.write(f"const int logn_top = {logn_top};\n\n")

        # P
        fc.write(f"const uint32_t P[{len(P)}] = {{\n")
        for i,val in enumerate(P):
            if i%elems_per_line==0:
                fc.write("   ")
            fc.write(f"{val},")
            if (i+1)%elems_per_line==0:
                fc.write("\n")
        if len(P)%elems_per_line!=0:
            fc.write("\n")
        fc.write("};\n\n")

        # omega_2048
        fc.write(f"const uint32_t omega_2048[{len(omega_2048)}] = {{\n")
        for i,val in enumerate(omega_2048):
            if i%elems_per_line==0:
                fc.write("   ")
            fc.write(f"{val},")
            if (i+1)%elems_per_line==0:
                fc.write("\n")
        if len(omega_2048)%elems_per_line!=0:
            fc.write("\n")
        fc.write("};\n\n")

        # omegas
        fc.write(f"const uint32_t omegas[{len(flat_omegas)}] = {{\n")
        for i,val in enumerate(flat_omegas):
            if i%elems_per_line==0:
                fc.write("   ")
            fc.write(f"{val},")
            if (i+1)%elems_per_line==0:
                fc.write("\n")
        if len(flat_omegas)%elems_per_line!=0:
            fc.write("\n")
        fc.write("};\n\n")

        # mu_omegas
        fc.write(f"const uint32_t mu_omegas[{len(flat_mu_omegas)}] = {{\n")
        for i,val in enumerate(flat_mu_omegas):
            if i%elems_per_line==0:
                fc.write("   ")
            fc.write(f"{val},")
            if (i+1)%elems_per_line==0:
                fc.write("\n")
        if len(flat_mu_omegas)%elems_per_line!=0:
            fc.write("\n")
        fc.write("};\n\n")

        # inverses_of_two
        fc.write(f"const uint32_t inverses_of_two[{len(inverses_of_two)}] = {{\n")
        for i,val in enumerate(inverses_of_two):
            if i%elems_per_line==0:
                fc.write("   ")
            fc.write(f"{val},")
            if (i+1)%elems_per_line==0:
                fc.write("\n")
        if len(inverses_of_two)%elems_per_line!=0:
            fc.write("\n")
        fc.write("};\n\n")

        for (name, poly) in polynomial_list:
            fc.write(f"const int32_t {name}[{len(poly)}] = {{\n")
            for i, val in enumerate(poly):
                if (i % elems_per_line) == 0:
                    fc.write("   ")
                fc.write(f"{val},")
                if ((i+1) % elems_per_line) == 0:
                    fc.write("\n")
            if (len(poly) % elems_per_line) != 0:
                    
                fc.write("\n")
                
            fc.write("};\n\n")

    print("Data generation done. You now have data.py, data.h, data.c with NTT_4 relevant arrays!")
