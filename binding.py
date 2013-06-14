{
   'conditions': [
    ['OS=="win"', {
      'variables': {
        'MAGICK_ROOT%': 'C:/Program Files/ImageMagick-6.8.5-Q16/', 
      }
    }, { # 'OS!="win"'
      'variables': {
        # no vars
      }
    }]
  ],
  "targets": [
    {
      "target_name": "imagemagick",
      "sources": [ "src/imagemagick.cc" ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      "conditions": [
        ['OS=="win"', {
          "libraries": [
            '-l<(MAGICK_ROOT)>/lib/CORE_RL_magick_.lib',
            '-l<(MAGICK_ROOT)>/lib/CORE_RL_Magick++_.lib',
            '-l<(MAGICK_ROOT)>/lib/CORE_RL_wand_.lib',
            '-l<(MAGICK_ROOT)>/lib/X11.lib'
          ],        
          'include_dirs': [
            '<(MAGICK_ROOT)/include',
          ]
        }], ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'OTHER_CFLAGS': [
              '<!@(Magick++-config --cflags)'
            ]
          },
          "libraries": [
             '<!@(Magick++-config --ldflags --libs)',
          ],
          'cflags': [
            '<!@(Magick++-config --cflags --cppflags)'
          ],
        }], { # not windows not mac
          "libraries": [
            '<!@(Magick++-config --ldflags --libs)',
          ],
          'cflags': [
            '<!@(Magick++-config --cflags --cppflags)'
          ],
        }]
    }