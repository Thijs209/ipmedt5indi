
const int BUTTON = 10;
const int LED = 6;
int data = 0;
char object = " ";
bool pressed = false;

void setup(){
    pinMode(BUTTON, INPUT_PULLUP);
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
}

void loop(){
  while(Serial.available() > 0){
    data =Serial.read();
  }

//  digitalWrite(LED,HIGH);

  switch (data) {
    case 'l':
      object = 'l';
      break;
    case '1' :
      if(object == 'l'){
        digitalWrite(LED, HIGH);
      }
      break;
    case '0':
      if(object == 'l') {
        digitalWrite(LED, LOW);
      }
  }
  
  if (!digitalRead(BUTTON)){
    delay(10);
    if(!digitalRead(BUTTON) && !pressed) {
      Serial.println('b');
      pressed = true;
      }
    } else {
        pressed = false;
    }
}
