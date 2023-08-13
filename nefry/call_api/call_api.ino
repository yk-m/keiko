#include <Nefry.h>
#include <WiFiClient.h>
#include "DHT.h"
#define DHTPIN D2     // what digital pin we're connected to

#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);

bool post_json(const char* host, const int port, const char* uri, String payload);

const int port = 80;
const char* host = "163.43.29.4";
const char* uri = "/api/v2/sensor/";

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

  String payload = "{\"temperature\":" + String(t) + ", \"humidity\":" + String(h) + "}";
  if (post_json(host, port, uri, payload)) {
    Nefry.setLed(0, 255, 0);
    Nefry.println("Your request was sent successfully!");
  } else {
    Nefry.setLed(255, 0, 0);
    Nefry.println("Not connected");
  }
  Nefry.ndelay(2000);
}

bool post_json(const char* host, const int port, const char* uri, String payload) {
  WiFiClient client;

  if (!client.connect(host, port)) {
    return false;
  }
  
  client.print("POST " + String(uri) + " HTTP/1.1" + "\r\n" +
               "Host: " + String(host) + "\r\n" +
               "User-Agent: ESP8266/1.0" + "\r\n" +
               "Connection: close" + "\r\n" +
               "Content-type: application/json" + "\r\n" +
               "Content-Length: " + String(payload.length()) + "\r\n" +
               "" + "\r\n" +
               payload + "\r\n"
               );
  delay(10);
  return true;
}

