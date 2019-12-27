int lectura; //Variable para guardar el mensaje recibido por serial
  
void setup(){
   //Inicializamos el servo y el Serial:
Serial.begin(9600);
}
  
void loop(){
   if (Serial.available() > 0)
   {
     lectura = Serial.parseInt(); //Leemos el serial
     Serial.flush();
     for (int i=0; i<lectura;i++){
     Serial.println(i);
   }
}
}
