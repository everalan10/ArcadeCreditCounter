int buttonPin = 2;
int lastState = HIGH;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT_PULLUP); // Botón → pin 2 y GND
}

void loop() {
  int state = digitalRead(buttonPin);

  // Detectar flanco: cuando pasa de NO presionado (HIGH) a presionado (LOW)
  if (state == LOW && lastState == HIGH) {
    Serial.println("1");   // Avisar a la PC que hubo "coin"
    delay(150);            // Anti-rebote sencillo
  }

  lastState = state;
}
