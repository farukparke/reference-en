from machine import pin,Timer
led=pin(28,pin.OUT)
timer)=Timer()File "<stdin>", line 3from m import pin,Timer
led=pin(28,pin.OUT)
timer)=Timer()File "<stdin>", line 3
deachinef blink(timer()
          def blink(timer):
          led.toggle()
          timer.init(freg=2.5,mode=Timer.PERIODIK,callback=blinFile "<stdin>", line 3k
def blink(timer()
          def blink(timer):
          led.toggle()
          timer.init(freg=2.5,mode=Timer.PERIODIK,callback=blinFile "<stdin>", line 3k{
  "packages": [
    {+
      "name": "ArduCAM_ESP32S_UNO",
      "maintainer": "ArduCAM",
      "websiteURL": "www.arducam.com",
      "email": "admin@arducam.com",
      "help": {
        "online": "http://esp32.com"
      },13
      "platforms": [
        {
          "name": "ArduCAM_ESP32S_UNO",
          "architecture": "esp32",
          "version": "2.0.0",
          "category": "ArduCAM_ESP32S_UNO",
          "url": "https://github.com/ArduCAM/ArduCAM_ESP32S_UNO/releases/download/v1.0.0/ArduCAM_ESP32S_UNO.zip",
          "archiveFileName": "ArduCAM_ESP32S_UNO.zip",
          "checksum": "SHA-256:FA398E6347ECF44DD80CF5DEE3167133D6B4EC9C67351D14A3C7E5EDC7E6DE2C",
          "size": "30810480",
          "help": {
            "online": ""
          },
          "boards": [
            {
              "name": "ArduCAM ESP32S UNO"
            }
          ],
          "toolsDependencies": [
            {
              "packager": "ArduCAM_ESP32S_UNO",
              "name": "xtensa-esp32-elf-gcc",
              "version": "1.22.0-80-g6c4433a-5.2.0"
            },
            {
              "packager": "ArduCAM_ESP32S_UNO",
              "name": "esptool",
              "version": "2.3.1"
            },
            {
              "packager": "ArduCAM_ESP32S_UNO",
              "name": "mkspiffs",
              "version": "0.2.3"
            }
          ]
        }
      ],
      "tools": [
        {
          "name": "xtensa-esp32-elf-gcc",
          "version": "1.22.0-80-g6c4433a-5.2.0",
          "systems": [
            {
              "host": "i686-mingw32",
              "url": "https://dl.espressif.com/dl/xtensa-esp32-elf-win32-1.22.0-80-g6c4433a-5.2.0.zip",
              "archiveFileName": "xtensa-esp32-elf-win32-1.22.0-80-g6c4433a-5.2.0.zip",
              "checksum": "SHA-256:f217fccbeaaa8c92db239036e0d6202458de4488b954a3a38f35ac2ec48058a4",
              "size": "125719261"
            },
            {
              "host": "x86_64-apple-darwin",
              "url": "https://dl.espressif.com/dl/xtensa-esp32-elf-osx-1.22.0-80-g6c4433a-5.2.0.tar.gz",
              "archiveFileName": "xtensa-esp32-elf-osx-1.22.0-80-g6c4433a-5.2.0.tar.gz",
              "checksum": "SHA-256:a4307a97945d2f2f2745f415fbe80d727750e19f91f9a1e7e2f8a6065652f9da",
              "size": "46517409"
            },
            {
              "host": "x86_64-pc-linux-gnu",
              "url": "https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz",
              "archiveFileName": "xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz",
              "checksum": "SHA-256:3fe96c151d46c1d4e5edc6ed690851b8e53634041114bad04729bc16b0445156",
              "size": "44219107"
            },
            {
              "host": "i686-pc-linux-gnu",
              "url": "https://dl.espressif.com/dl/xtensa-esp32-elf-linux32-1.22.0-80-g6c4433a-5.2.0.tar.gz",
              "archiveFileName": "xtensa-esp32-elf-linux32-1.22.0-80-g6c4433a-5.2.0.tar.gz",
              "checksum": "SHA-256:b4055695ffc2dfc0bcb6dafdc2572a6e01151c4179ef5fa972b3fcb2183eb155",
              "size": "45566336"
            }
          ]
        },
        {
          "name": "esptool",
          "version": "2.3.1",
          "systems": [
            {
              "host": "i686-mingw32",
              "url": "https://dl.espressif.com/dl/esptool-2.3.1-windows.zip",
              "archiveFileName": "esptool-2.3.1-windows.zip",
              "checksum": "SHA-256:c187763d0faac7da7c30a292a23c759bbc256fcd084dc8846ed284000cb0fe29",
              "size": "3396085"
            },
            {
              "host": "x86_64-apple-darwin",
              "url": "https://dl.espressif.com/dl/esptool-2.3.1-macos.tar.gz",
              "archiveFileName": "esptool-2.3.1-macos.tar.gz",
              "checksum": "SHA-256:cd922418f02e0ca11dc066b36a22646a1b441da00d762b4464ca598c902c5ecb",
              "size": "3810932"
            },
            {
              "host": "x86_64-pc-linux-gnu",
              "url": "https://dl.espressif.com/dl/esptool-2.3.1-linux.tar.gz",
              "archiveFileName": "esptool-2.3.1-linux.tar.gz",
              "checksum": "SHA-256:cff30841dad80ed5d7d2d58a31843b63afa57528979a9c839806568167691d8e",
              "size": "39563"
            },
            {
              "host": "i686-pc-linux-gnu",
              "url": "https://dl.espressif.com/dl/esptool-2.3.1-linux.tar.gz",
              "archiveFileName": "esptool-2.3.1-linux.tar.gz",
              "checksum": "SHA-256:cff30841dad80ed5d7d2d58a31843b63afa57528979a9c839806568167691d8e",
              "size": "39563"
            },
            {
              "host": "arm-linux-gnueabihf",
              "url": "https://dl.espressif.com/dl/esptool-2.3.1-linux.tar.gz",
              "archiveFileName": "esptool-2.3.1-linux.tar.gz",
              "checksum": "SHA-256:cff30841dad80ed5d7d2d58a31843b63afa57528979a9c839806568167691d8e",
              "size": "39563"
            }
          ]
        },
        {
          "name": "mkspiffs",
          "version": "0.2.3",
          "systems": [
            {
              "host": "i686-mingw32",
              "url": "https://github.com/igrr/mkspiffs/releases/download/0.2.3/mkspiffs-0.2.3-arduino-esp32-win32.zip",
              "archiveFileName": "mkspiffs-0.2.3-arduino-esp32-win32.zip",
              "checksum": "SHA-256:b647f2c2efe6949819c85ea9404271b55c7c9c25bcb98d3b98a1d0ba771adf56",
              "size": "249809"
            },
            {
              "host": "x86_64-apple-darwin",
              "url": "https://github.com/igrr/mkspiffs/releases/download/0.2.3/mkspiffs-0.2.3-arduino-esp32-osx.tar.gz",
              "archiveFileName": "mkspiffs-0.2.3-arduino-esp32-osx.tar.gz",
              "checksum": "SHA-256:9f43fc74a858cf564966b5035322c3e5e61c31a647c5a1d71b388ed6efc48423",
              "size": "130270"
            },
            {
              "host": "i386-apple-darwin",
              "url": "https://github.com/igrr/mkspiffs/releases/download/0.2.3/mkspiffs-0.2.3-arduino-esp32-osx.tar.gz",
              "archiveFileName": "mkspiffs-0.2.3-arduino-esp32-osx.tar.gz",
              "checksum": "SHA-256:9f43fc74a858cf564966b5035322c3e5e61c31a647c5a1d71b388ed6efc48423",
              "size": "130270"
            },
            {
              "host": "x86_64-pc-linux-gnu",
              "url": "https://github.com/igrr/mkspiffs/releases/download/0.2.3/mkspiffs-0.2.3-arduino-esp32-linux64.tar.gz",
              "archiveFileName": "mkspiffs-0.2.3-arduino-esp32-linux64.tar.gz",
              "checksum": "SHA-256:5e1a4ff41385e842f389f6b5254102a547e566a06b49babeffa93ef37115cb5d",
              "size": "50646"
            },
            {
              "host": "i686-pc-linux-gnu",
              "url": "https://github.com/igrr/mkspiffs/releases/download/0.2.3/mkspiffs-0.2.3-arduino-esp32-linux32.tar.gz",
              "archiveFileName": "mkspiffs-0.2.3-arduino-esp32-linux32.tar.gz",
              "checksum": "SHA-256:464463a93e8833209cdc29ba65e1a12fec31718dc10075c195a2445b2c3f6cb0",
              "size": "48751"
            },
            {
              "host": "arm-linux-gnueabihf",
              "url": "https://github.com/igrr/mkspiffs/releases/download/0.2.3/mkspiffs-0.2.3-arduino-esp32-linux-armhf.tar.gz",
              "archiveFileName": "mkspiffs-0.2.3-arduino-esp32-linux-armhf.tar.gz",
              "checksum": "SHA-256:ade3dc00117912ac08a1bdbfbfe76b12d21a34bc5fa1de0cfc45fe7a8d0a0185",
              "size": "40665"
            }
          ]
        }
      ]
    }
  ]
}
                     