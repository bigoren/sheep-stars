/*
 UDPSendReceiveString:
 This sketch receives UDP message strings, prints them to the serial port
 and sends an "acknowledge" string back to the sender

 A Processing sketch is included at the end of file that can be used to send
 and received messages for testing with a computer.

 created 21 Aug 2010
 by Michael Margolis

 This code is in the public domain.
 */


#include <SPI.h>         // needed for Arduino versions later than 0018
#include <Ethernet.h>
#include <EthernetUdp.h>         // UDP library from: bjoern@cs.stanford.edu 12/30/2008

#include <FastLED.h>
#define NUM_LEDS 300
#define PACKET_SIZE (NUM_LEDS * 3 + 4)
#define DATA_PIN 6

CRGB leds[NUM_LEDS];

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xC9 //last byte should be the hex of the last byte of the ip address
};
IPAddress ip( 192,168,1,201 );

unsigned int localPort = 2000;      // local port to listen on

// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;

void setup() {

  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  memset(leds, 0, NUM_LEDS * 3);
  FastLED.show();

  // disable SD
  pinMode(4,OUTPUT);
  digitalWrite(4,HIGH);

  // start the Ethernet and UDP:
  Ethernet.begin(mac, ip);
  Udp.begin(localPort);

  Serial.begin(9600);
}

void loop() {
  // if there's data available, read a packet
  int packetSize = Udp.parsePacket();
  if (packetSize >= PACKET_SIZE) {
/*    Serial.print("Received packet of size ");
    Serial.println(packetSize);
    Serial.print("From ");
    IPAddress remote = Udp.remoteIP();
    for (int i = 0; i < 4; i++) {
      Serial.print(remote[i], DEC);
      if (i < 3) {
        Serial.print(".");
      }
    }
    Serial.print(", port ");
    Serial.println(Udp.remotePort());*/

    char universe;
    Udp.read(&universe, 1);
    if(universe == 0)
    {
      char frameNum[3];
      Udp.read((char *)frameNum, 3);
      // Nothing to do with frameNum
      
      Udp.read((char *)leds, PACKET_SIZE);
      FastLED.show();      
    }
    /*Serial.println("Contents:");
    Serial.println(packetBuffer);

    // send a reply to the IP address and port that sent us the packet we received
    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
    Udp.write(ReplyBuffer);
    Udp.endPacket();*/
  }
}


