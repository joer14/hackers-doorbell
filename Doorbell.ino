/* 
 *  Hackers Doorbell
 *  Joe Rowley
 *  April, 2017
*/

void setup() {                
  pinMode(12, INPUT);
  Keyboard.begin();
}

void mute() {
   Keyboard.press(KEY_MEDIA_MUTE);
   Keyboard.release(KEY_MEDIA_MUTE);
}

void pause() {
  Keyboard.press(KEY_MEDIA_PLAY_PAUSE);
  Keyboard.release(KEY_MEDIA_PLAY_PAUSE);
}

void invert() {
  Keyboard.press(KEY_LEFT_GUI); // 'Apple' Key
  Keyboard.press(KEY_LEFT_ALT); 
  Keyboard.press(KEY_LEFT_CTRL);
  Keyboard.press('8');
  delay(100);
  Keyboard.releaseAll();
}
void flash(int iters) {
  for (int i=0; i<iters;i++){
    invert();
    delay(100);
    invert();
    delay(100);
  }
}

void loop()                     
{
  if (digitalRead(12) != HIGH) {
    Serial.println("Button pressed!!!");
    pause();
    mute();
    flash(3);
    mute();
  }
  delay(50);
}
