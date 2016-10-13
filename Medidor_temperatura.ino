const int LM35 = A0; // Define o pino que lera a saída do LM35
float temperatura; // Variável que armazenará a temperatura medida
int i = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

int iniciar = 0;
void loop() {
  // put your main code here, to run repeatedly:


  temperatura = (float(analogRead(LM35))*5/(1023))/0.01;
  Serial.println(temperatura);
  //delay(300000);
  delay(1000);
}
