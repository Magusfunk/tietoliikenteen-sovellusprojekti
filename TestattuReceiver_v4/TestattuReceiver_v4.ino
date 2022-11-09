// ask_reliable_datagram_server.pde
// -*- mode: C++ -*-
// Example sketch showing how to create a simple addressed, reliable messaging server
// with the RHReliableDatagram class, using the RH_ASK driver to control a ASK radio.
// It is designed to work with the other example ask_reliable_datagram_client
// Tested on Arduino Mega, Duemilanova, Uno, Due, Teensy, ESP-12
#include <arduino.h>

#define DEBUGPRINT 0
/*
 Huomioita:
 Jostain syystä arduinon delay() funktio ei 
 toimi oikein radioheadin kirjaston kanssa.
 Viiveen on siksi joutunut tekemään typerällä luupilla
 
 */
#include <RHReliableDatagram.h>
#include <RH_ASK.h>
#include <SPI.h>

#define TRANSMITTER_ADDRESS 254  // Teemun ja Karin vastaanottimen osoite


// Singleton instance of the radio driver
RH_ASK driver;
RHReliableDatagram manager(driver, TRANSMITTER_ADDRESS);

void setup() 
{ 
  Serial.begin(9600);
  if (!manager.init())
    Serial.println("init failed");
}

uint8_t data[] = "ACKmessage";
uint8_t buf[RH_ASK_MAX_MESSAGE_LEN];


void sendReceivedToDatabase(uint8_t * msg, int len, int groupId,int msgId, int flags )
{
   uint16_t xAcceleration = ((msg[0]<<8)&0xff00) + (msg[1]&0x00ff);
   uint16_t yAcceleration = ((msg[2]<<8)&0xff00) + (msg[3]&0x00ff);
   uint16_t zAcceleration = ((msg[4]<<8)&0xff00) + (msg[5]&0x00ff);
   char measName[len-5];
   for(int i = 0;i<len-5;i++)
   {
      measName[i]=msg[6+i];
   }
   Serial.print("groupID = ");
   Serial.println(groupId);
   Serial.print("message ID = ");
   Serial.println(msgId);
   Serial.print("message flags = ");
   Serial.println(flags);
   Serial.print("xAcceleration = ");
   Serial.println(xAcceleration);
   Serial.print("yAcceleration = ");
   Serial.println(yAcceleration);
   Serial.print("zAcceleration = ");
   Serial.println(zAcceleration);
   Serial.print("Mittauksen nimi = ");
   Serial.println(measName);
}


void loop()
{
  while(1)
  {
    driver.setModeRx();
    if (manager.available())
    {
      // Wait for a message addressed to us from the client
      uint8_t len = sizeof(buf);
      uint8_t from;
      uint8_t to = TRANSMITTER_ADDRESS;  // Vastaanotetaan 254 osoitteeseen lähetetyt 
      uint8_t id;
      uint8_t flags;
      if (manager.recvfrom(buf, &len, &from, &to, &id,&flags))
      {
         sendReceivedToDatabase(buf, len,from,id,flags);
         #if DEBUGPRINT
         Serial.println((char*)buf);
         Serial.print("Lähetettiin osoitteesta = ");
         Serial.println(from);
         Serial.print("ID = ");
         Serial.println(id);
         Serial.print("flags = ");
         Serial.println(flags);
         #endif
         driver.setModeTx();

         volatile unsigned long start = 400000;
         while(start>0)
         {
            start--;
         }
         
         manager.setHeaderTo(from); // reply to how sent
         manager.setHeaderFrom(TRANSMITTER_ADDRESS);
         manager.setHeaderId(id); // send same id
         manager.setHeaderFlags(flags);

         
         manager.sendto(data,sizeof(data),from);
         manager.waitPacketSent();

         //manager.sendto(data,sizeof(data),from);
         //manager.waitPacketSent();
         

      } // endif got message
    }   // endif manager available
  }   // end while
}
