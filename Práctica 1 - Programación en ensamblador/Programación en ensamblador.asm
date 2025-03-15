JMP boot

stackTop    EQU 0xFF          ; Puntero de pila
textDisplay EQU 0x2E0         ; Dirección de la pantalla de texto
gfxDisplay  EQU 0x300         ; Dirección base de la pantalla gráfica

; Definir posiciones para la animación (dos frames)
frame0      EQU 0x300         ; Posición 1
frame1      EQU 0x304         ; Posición 2 (desplazada 4 bytes a la derecha)

hello:      DB "Hola profe!"
            DB 0              ; Terminador de cadena

; Sprite de 4x4 (16 bytes totales)
sprite:
    DB "\xFF\xFF\xFF\xFF\xFF\x1F\x1F\x1F"
	DB "\x1F\x1F\xFF\xFF\xFF\xFF\xFF\xFF"
	DB "\xFF\xFF\xFF\xFF\x1F\x1F\x1F\x1F"
	DB "\x1F\x1F\x1F\x1F\x1F\xFF\xFF\xFF"
	DB "\xFF\xFF\xFF\xFF\x8C\x8C\x8C\xF4"
	DB "\xF4\x8C\xF4\xFF\xFF\xFF\xFF\xFF"
	DB "\xFF\xFF\xFF\x8C\xF4\x8C\xF4\xF4"
	DB "\xF4\x8C\xF4\xF4\xF4\xFF\xFF\xFF"
	DB "\xFF\xFF\xFF\x8C\xF4\x8C\x8C\xF4"
	DB "\xF4\xF4\x8C\xF4\xF4\xF4\xFF\xFF"
	DB "\xFF\xFF\xFF\x8C\x8C\xF4\xF4\xF4"
	DB "\xF4\x8C\x8C\x8C\x8C\xFF\xFF\xFF"
	DB "\xFF\xFF\xFF\xFF\xFF\xF4\xF4\xF4"
	DB "\xF4\xF4\xF4\xF4\xFF\xFF\xFF\xFF"
	DB "\xFF\xFF\xFF\xFF\x8C\x8C\xC4\x8C"
	DB "\x8C\x8C\xFF\xFF\xFF\xFF\xFF\xFF"
	DB "\xFF\xFF\xFF\x8C\x8C\x8C\xC4\x8C"
	DB "\x8C\xC4\x8C\x8C\x8C\xFF\xFF\xFF"
	DB "\xFF\xFF\x8C\x8C\x8C\x8C\xC4\xC4"
	DB "\xC4\xC4\x8C\x8C\x8C\x8C\xFF\xFF"
	DB "\xFF\xFF\xF4\xF4\x8C\xC4\x00\xC4"
	DB "\xC4\x00\xC4\xC4\xF4\xF4\xFF\xFF"
	DB "\xFF\xFF\xF4\xF4\xF4\xC4\xC4\xC4"
	DB "\xC4\xC4\xC4\xF4\xF4\xF4\xFF\xFF"
	DB "\xFF\xFF\xF4\xF4\xC4\xC4\xC4\xC4"
	DB "\xC4\xC4\xC4\xC4\xF4\xF4\xFF\xFF"
	DB "\xFF\xFF\xFF\xFF\xC4\xC4\xC4\xFF"
	DB "\xFF\xC4\xC4\xC4\xFF\xFF\xFF\xFF"
	DB "\xFF\xFF\xFF\x00\x00\x00\xFF\xFF"
	DB "\xFF\xFF\x00\x00\x00\xFF\xFF\xFF"
	DB "\xFF\xFF\x00\x00\x00\x00\xFF\xFF"
	DB "\xFF\xFF\x00\x00\x00\x00\xFF\xFF"

boot:
        ; Inicializa la pila
        MOV SP, stackTop

        ; Imprime mensaje en la pantalla de texto
        MOV C, hello        ; C apunta a la cadena "Hola Mundo!"
        MOV D, textDisplay  ; D apunta al inicio de la pantalla de texto
        CALL printText

        ; Realiza animación en la pantalla gráfica
        CALL drawSprite

        HLT                 ; Detener ejecución


printText:
        PUSH A
        PUSH B
        MOV B, 0

pt_loop:
        MOVB AL, [C]        ; Leer carácter de la cadena
        CMPB AL, 0          ; ¿Terminador?
        JZ pt_done          ; Si es 0, fin del texto

        MOVB [D], AL        ; Escribir carácter en la pantalla
        INC C
        INC D
        JMP pt_loop

pt_done:
        POP B
        POP A
        RET


drawSprite:
        PUSH A
        PUSH B
        MOV B, 0            ; Contador de ciclos de animación

animLoop:
        ; --- Dibuja el sprite en frame0 ---
        MOV D, frame0       ; Selecciona posición frame0
        MOV C, sprite       ; C apunta al sprite
        MOV A, 0x10         ; 16 bytes a copiar
drawLoop0:
        MOVB AL, [C]        ; Leer byte del sprite
        MOVB [D], AL        ; Escribir en la pantalla gráfica
        INC C
        INC D
        DEC A
        JNZ drawLoop0

        CALL delay_ms       ; Retardo entre frames

        ; --- Dibuja el sprite en frame1 ---
        MOV D, frame1       ; Selecciona posición frame1
        MOV C, sprite       ; Reinicia C al inicio del sprite
        MOV A, 0x10         ; 16 bytes a copiar
drawLoop1:
        MOVB AL, [C]
        MOVB [D], AL
        INC C
        INC D
        DEC A
        JNZ drawLoop1

        CALL delay_ms       ; Retardo entre frames

        INC B               ; Incrementa contador de ciclos
        MOV A, B
        CMP A, 4           ; Realiza 4 ciclos de animación
        JNZ animLoop

        POP B
        POP A
        RET


delay_ms:
        PUSH A
        MOV A, 0xFF
delay_loop:
        DEC A
        JNZ delay_loop
        POP A
        RET
