#include<ESP8266_Lib.h>
#include<Servo.h>
Servo Serve;
int MotorLeft = 7;
int MotorRight = 8;
String Ssid = "JETBooWifi";
String Pass = "buddy54321_";
//int PrevOfLeft = 0;
//int PrevOfRight = 0;
ESP8266 Connection(&Serial);
int WhatsAvailable;

void setup() {
  // Setup of WIFI
  Serial.begin(500000);
  delay(500);
  Connection.run();
  delay(500);
  pinMode(MotorLeft, OUTPUT);
  analogWrite(MotorLeft, LOW);
  pinMode(MotorRight, OUTPUT);
  analogWrite(MotorRight, LOW);
  Serial.println("Starting");
  while (true) {
    Connection.setUart((long int)500000, 3);
    if (!Connection.kick())
    {
      Serial.println("Wait");
      delay(500);
    }
    else
    {
      break;
    }
  }
  Serial.println("Working");
  Connection.setOprToSoftAP();
  bool Wait = Connection.disableMUX();
  if (Wait)
  {
    Serial.println("Mux Disabled");
  }
  Connection.setSoftAPParam(Ssid, Pass, 1, 3);
  // (0 - OPEN, 1 - WEP, *  2 - WPA_PSK, 3 - WPA2_PSK, 4 - WPA_WPA2_PSK, default: 4) dont use 1 it will end up in error
  delay(1000);
  String IP = "192.168.4.2";
  uint32_t Port = 55860;
  bool Connected = false;
  while(!Connected){
  Connected = Connection.createTCP(IP, Port);
  }
  Connected = false;
  while (!Connected)
  {
    Connection.send("12", 2);
    delay(200);
    String Data;
    if (Serial.available())
      Data = Serial.readString();
    if (Data.indexOf("+IPD") != -1)
    {
      Connected = true;
    }
  }
  Serial.print("Connected to ");
  Serial.print(IP);
  Serial.print(" at port ");
  Serial.println(Port);
  pinMode(LED_BUILTIN, OUTPUT);

  delay(500);
  //    Serve.attach(4);
  //    Serve.write(80);
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
//    Serial.flush();
    int Data = Serial.parseInt();
    Connection.eATCIBUFRESET();    
    Serial.println(Data);
    if (Data != 0){
    if (Data == 234 || Data == 324 || Data == 423 || Data == 243 || Data == 342 || Data == 432 || Data == 1)
    {
//      Connection.run();
      digitalWrite(MotorRight, 0);
      digitalWrite(MotorLeft, 0);
    }
    else if (Data == 23 || Data == 32)
    {
//      Connection.run();
      digitalWrite(MotorRight, 1);
      digitalWrite(MotorLeft, 0);
    }
    else if (Data == 24 || Data == 42)
    {
//      Connection.run();
      digitalWrite(MotorRight, 0);
      digitalWrite(MotorLeft, 1);
    }
    else if (Data == 2)
    {
//      Connection.run();
      digitalWrite(MotorRight, 1);
      digitalWrite(MotorLeft, 1);
    }
    
    Connection.sendFromFlash("A", 1);
    
}
}
