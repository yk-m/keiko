#include <Nefry.h>
#include <WiFiClient.h>
#include "DHT.h"
#define DHTPIN D2     // what digital pin we're connected to

#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);

const int httpPort = 80;
const char* host = "163.43.29.4";
const char* uri = "/api/v2/temperature/";

void setup() {
  Nefry.setProgramName("Call API");
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Nefry.println("Failed to read from DHT sensor!");
    return;
  }

  WiFiClient client;

  if (!client.connect(host, httpPort)) {
    Nefry.setLed(255, 0, 0);
    Nefry.ndelay(2000);
    Nefry.println("Not connected");
    return;
  }

  String payload = "{\"degree\":" + String(t) + "}";

  client.print(
               String("POST ") + uri + " HTTP/1.1\r\n" +
               "Host: " + String(host) + "\r\n" +
               "Connection: close\r\n" +
               "Content-type: application/json\r\n" +
               "Content-Length: " + String(payload.length()) + "\r\n" + 
               "\r\n" +
               payload + "\r\n"
               );

  Nefry.setLed(0, 255, 0);
  Nefry.ndelay(2000);
  Nefry.println("Your request was sent successfully!");
}

