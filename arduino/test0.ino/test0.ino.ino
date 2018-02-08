
const int buf_size = 32;
char buf[buf_size];
int len = 0;

//char endChar= '.';
char endChar= '\n';

void setup() {
  // initialize serial:
  Serial.begin(9600);
  //Serial.print("Start.");
}

void loop() {
  int cmdId = getCmdId();
  switch(cmdId) {
    case 1:
      Serial.print("bbb");
      Serial.write(endChar);
      Serial.print("ccc");
      Serial.write(endChar);
    break;
    case 2:
      Serial.print("123");
      Serial.write(endChar);
    break;
    case 3:
      Serial.print("333");
      Serial.write(endChar);
    break;
  }
}

int getCmdId() {
  while(true) {
    while (Serial.available() <= 0) {}
    if(len < buf_size) {
      char inByte = Serial.read();
      if(inByte == endChar) {
        //Serial.print("OK");
        return parseCmdId();
      } else {
        buf[len] = inByte;
        len++;
      }
    } else {
      Serial.println("ERROR");
      len = 0;
    }
  }
}

int parseCmdId() {
  int cmdId;
  switch(buf[0]) {
    case 'a':
      if((len == 3) && (buf[1] == 'a') && (buf[2] == 'a')) cmdId = 1;
      else cmdId = 0;
    break;
    case 'b':
      if((len == 3) && (buf[1] == 'b') && (buf[2] == 'b')) cmdId = 2;
      else cmdId = 0;
    break;
    case 'c':
      if((len == 3) && (buf[1] == 'c') && (buf[2] == 'c')) cmdId = 3;
      else cmdId = 0;
    break;
    default:
      cmdId = 0;
  }
  len = 0;
  return cmdId;
}
