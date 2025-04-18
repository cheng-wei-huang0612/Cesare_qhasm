###############################################################################
# Makefile for ntt_4par_len4
#
# 產生可執行檔：test-ntt_4par_len4-program
#
# 包含：
# 1. 多個 .S 檔（ct_4par_len2.S、gs_4par_len2.S、gs_4par_len2_last.S、
#    mul_inv_4.S、pointmul.S）
# 2. C 檔（test-ntt_4par_len4.c、data.c）
# 3. （可選）如要從 .q 產生 .S，可在 Makefile 中加上相應規則
###############################################################################

# 專案名稱
NAME    := ntt_4par_len4

# 編譯器、標準旗標
CC      := gcc
CFLAGS  := -O2 -Wall
LDLIBS  :=

# QHASM 腳本 (如需從 .q → .S 時才會使用)
QHASM   := qhasm-ARMv8  # or ./qhasm-armv8, depending on environment

# 生成的可執行檔名稱
TARGET  := test-$(NAME)-program

# -----------------------------------------------------------------------------
# 原始碼清單
# -----------------------------------------------------------------------------

# 1) 組合語言檔 .S
ASMSRC := ct_4par_len2.S \
          gs_4par_len2.S \
          gs_4par_len2_last.S \
          mul_inv_4.S \
          pointmul.S

# 自動把 .S 檔名對應成 .o
ASMOBJ := $(ASMSRC:.S=.o)

# 2) C 檔
CSRCS := data.c \
         test-$(NAME).c

# 自動把 .c 對應成 .o
COBJS := $(CSRCS:.c=.o)

# -----------------------------------------------------------------------------
# 如要從 .q → .S, 可以在此定義對應規則
# -----------------------------------------------------------------------------
# 例如：
# ct_4par_len2.S: ct_4par_len2.q
# 	$(QHASM) < $< > $@
#
# gs_4par_len2.S: gs_4par_len2.q
# 	$(QHASM) < $< > $@
#
# ... etc. 視需要自行加上

# -----------------------------------------------------------------------------
# 最終目標：$(TARGET)
# -----------------------------------------------------------------------------
all: $(TARGET)

$(TARGET): $(ASMOBJ) $(COBJS)
	$(CC) $(CFLAGS) $^ -o $@ $(LDLIBS)

# -----------------------------------------------------------------------------
# 一般規則：組譯 .S → .o
# -----------------------------------------------------------------------------
%.o: %.S
	$(CC) $(CFLAGS) -c $< -o $@

# -----------------------------------------------------------------------------
# 一般規則：編譯 .c → .o
# -----------------------------------------------------------------------------
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# -----------------------------------------------------------------------------
# 清理
# -----------------------------------------------------------------------------
.PHONY: clean
clean:
	rm -f $(TARGET) *.o *.S data.py data.c data.h
