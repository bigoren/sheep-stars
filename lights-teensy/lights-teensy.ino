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


/*
 * The frames are assumed to arrive in our internal protocol which is: 
 * First byte is the universe
 * Next 3 bytes are the frame id (starts with zero and advances).
 * This id will allow us to trace lost packages and to syncrhonize different universes.
 * Next 900 bytes are group of 300 pixels (fixed). 
 * For each pixel, the first byte is Red, second is Green, third is Blue.
 */

#include <SPI.h>         // needed for Arduino versions later than 0018
#include <Ethernet.h>
#include <EthernetUdp.h>         // UDP library from: bjoern@cs.stanford.edu 12/30/2008

#include <OctoWS2811.h>
const int ledsPerStrip = 600;
const int pixelsInPacket = 300;
#define PACKET_SIZE (pixelsInPacket * 3 + 1 + 3)

const int totalUniverses = 3;
const int minUniverse = 0;
bool universesReceived[totalUniverses];

DMAMEM int displayMemory[ledsPerStrip*6];
int drawingMemory[ledsPerStrip*6];

const int config = WS2811_GRB | WS2811_800kHz;
OctoWS2811 leds(ledsPerStrip, displayMemory, drawingMemory, config);

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xD2 //last byte should be the hex of the last byte of the ip address
};
IPAddress ip( 192,168,1,210 );

unsigned int localPort = 2000;      // local port to listen on

// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;

void setup() {

  // start octows2811
  leds.begin();
  SendToStrip();

  // start the Ethernet and UDP:
  Ethernet.begin(mac, ip);
  Udp.begin(localPort);

  Serial.begin(9600);
  Serial.println("hello");
}

void loop() {
  // if there's data available, read a packet
  int packetSize = Udp.parsePacket();
  if (packetSize >= PACKET_SIZE) {    
    char tempBuf[PACKET_SIZE];
    Udp.read((char *)tempBuf, PACKET_SIZE);

    char universe = tempBuf[0];
    int startPixelId = UniverseToPixelNumber(universe);
    if(startPixelId != -1)
    {
      int currPixelIndex = startPixelId;
      for(int i=0; i<pixelsInPacket; i++, currPixelIndex++)
      {
        int pixelRgbStart = 4 + i*3;
        unsigned int color = ((unsigned int)tempBuf[pixelRgbStart] << 16) | ((unsigned int)tempBuf[pixelRgbStart + 1] << 8) | ((unsigned int)tempBuf[pixelRgbStart + 2]);
        leds.setPixel(currPixelIndex, color);
      }

      bool shouldUpdate = true;
      for(int i=0; i<totalUniverses; i++)
      {
        if(universesReceived[i] == false)
          shouldUpdate = false;
      }

      if(shouldUpdate)
      {
        SendToStrip();
      }
    }
  }
}

void SendToStrip()
{
  for(int i=0; i<totalUniverses; i++)
    universesReceived[i] = false;
  leds.show();
}

int UniverseToPixelNumber(char universe)
{
  switch(universe)
  {
    case 0: 
      universesReceived[0] = true;
      return 0;
      
    case 1: 
      universesReceived[1] = true;
      return ledsPerStrip;

    case 2: 
      universesReceived[2] = true;
      return ledsPerStrip + pixelsInPacket;
      
    default: return -1;
  }
}

