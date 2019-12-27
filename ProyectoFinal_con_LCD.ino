#include <Wire.h>
#include <LiquidCrystal_I2C.h> //Se incluyó para verificar que los datos de la lectura son correctos
LiquidCrystal_I2C lcd(0X27, 16, 2);

int lectura; //Variable para guardar el mensaje recibido por serial
  
void setup(){
   //Inicializamos el servo y el Serial:
lcd.begin ();
Serial.begin (9600);
lcd.backlight();

}
  
void loop(){
   if (Serial.available() > 0)
   {
     lectura = Serial.parseInt(); //Leemos el serial
     lcd.print(lectura);
     Serial.flush();
     for (int i=0; i<lectura;i++){
     Serial.println(i);
   }
}
}
