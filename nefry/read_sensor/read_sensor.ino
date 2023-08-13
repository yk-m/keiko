#include <Nefry.h>
#include "DHT.h"
#define DHTPIN D2     // what digital pin we're connected to

#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Nefry.println("DHTxx test!");
  Nefry.setLed(0,0,0);
  dht.begin();
  Nefry.setProgramName("read sensor2");
}

void loop() {
  Nefry.ndelay(2000);
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);

  if (isnan(h) || isnan(t) || isnan(f)) {
    Nefry.println("Failed to read from DHT sensor!");
    return;
  }

  float hif = dht.computeHeatIndex(f, h);
  float hic = dht.computeHeatIndex(t, h, false);

  Nefry.print("Humidity: ");
  Nefry.print(h);
  Nefry.print(" %\t");
  Nefry.print("Temperature: ");
  Nefry.print(t);
  Nefry.print(" *C ");
  Nefry.print(f);
  Nefry.print(" *F\t");
  Nefry.print("Heat index: ");
  Nefry.print(hic);
  Nefry.print(" *C ");
  Nefry.print(hif);
  Nefry.println(" *F");

  //湿度が60%を超えたらLEDが青く光り、59%以下だと赤く光る
  if(h > 60){
     Nefry.setLed(0,0,200);
  }else{
     Nefry.setLed(200,0,0);
  }
}
