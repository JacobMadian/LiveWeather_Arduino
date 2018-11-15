#include <FastLED.h>
#define NUM_LEDS 24
#define LED_PIN 2

CRGB leg[NUM_LEDS];

void setup() {
  FastLED.addLEDS<NEOPIXEL, LED_PIN>(led, NUM_LEDS);

    for(int i = 0; i < NUM_LEDS; i++) {
      led[i] = CRGB(0, 0, 255);
    }

    FastLED.show();
}

void rain(int val) {
  for 
}

void loop() {
  // put your main code here, to run repeatedly:

}
