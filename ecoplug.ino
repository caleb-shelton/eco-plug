bool on = false;

void setup() {
  pinMode(8, OUTPUT); // Arduino will be sending control signals over port 8
  digitalWrite(8,HIGH); // set the initial value of the relay to off
  Serial.begin(115200); // baud rate of 115200
}

void loop() {
//  If there is serial data received, read the data and
//  if the data is the string 's' then turn on the relay
//  through port 8. If the relay is already turned on then
//  turn it off
  if (Serial.available() > 0) {
    if (Serial.read() == 's') {
      if (on == false) {
        digitalWrite(8, LOW);
        on = true;
      } else {
        digitalWrite(8, HIGH);
        on = false;
      }
    }
  }
}
