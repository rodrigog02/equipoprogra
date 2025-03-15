JMP boot

stackTop    EQU 0xFF          ; Puntero de pila
textDisplay EQU 0x2E0         ; Dirección de la pantalla de texto
gfxDisplay  EQU 0x300         ; Dirección base de la pantalla gráfica

; Definir posiciones para la animación (dos frames)
frame0      EQU 0x300         ; Posición 1
frame1      EQU 0x304         ; Posición 2 (desplazada 4 bytes a la derecha)

hello:      DB "Hola profe!"
            DB 0              ; Terminador de cadena

