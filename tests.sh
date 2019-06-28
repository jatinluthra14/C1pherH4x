#!/bin/bash

# bacon_encode
(if [[ $(python C1pherH4x.py -c bacon -e -s -pt 'ILOUEBACONDONTYOU' | grep -c 'ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB') -eq 1 ]]; then echo -e "\e[32m\e[1mBacon Encode Working Successfully!"; else echo -e "\e[31m\e[1mBacon Encode not Working :("; fi) &

# bacon_decode
(if [[ $(python C1pherH4x.py -d -s -ct 'ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB' | grep -c 'ILOUEBACONDONTYOU') -eq 1 ]]; then echo -e "\e[32m\e[1mBacon Decode Working Successfully!"; else echo -e "\e[31m\e[1mBacon Decode not Working :("; fi) &

# base64_encode
(if [[ $(python C1pherH4x.py -c base64 -e -s -pt 'CTF{FlaggyWaggyRaggy}' | grep -Pzc '(?s)^Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9\n$') -eq 1 ]]; then echo -e "\e[32m\e[1mBase64 Encode Working Successfully!"; else echo -e "\e[31m\e[1mBase64 Encode not Working :("; fi) &

# base64_decode
(if [[ $(python C1pherH4x.py -d -s -ct "Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9" -ff "CTF{.*}" | grep -Pzc '(?s)^CTF{FlaggyWaggyRaggy}\n$') -eq 1 ]]; then echo -e "\e[32m\e[1mBase64 Decode Working Successfully!"; else echo -e "\e[31m\e[1mBase64 Decode not Working :("; fi) &

# binary_encode
(if [[ $(python C1pherH4x.py -s -e -pt "CTF{Bit_Flippin}" -c binary | grep -Pzc '(?s)^1000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101\n$') -eq 1 ]]; then echo -e "\e[32m\e[1mBinary Encode Working Successfully!"; else echo -e "\e[31m\e[1mBinary Encode not Working :("; fi) &

# binary_decode
(if [[ $(python C1pherH4x.py -s -d -ct "01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101" -ff "CTF{.*}" | grep -Pzc '(?s)^CTF{Bit_Flippin}\n$') -eq 1 ]]; then echo -e "\e[32m\e[1mBinary Decode Working Successfully!"; else echo -e "\e[31m\e[1mBinary Decode not Working :("; fi) &

# morse_encode
(if [[ $(python C1pherH4x.py -c morse -e -s -pt 'FLAGSAMUELMORSEISCOOLBYTHEWAYILIKECHEES' | grep -c '..-. .-.. .- --. ... .- -- ..- . .-.. -- --- .-. ... . .. ... -.-. --- --- .-.. -... -.-- - .... . .-- .- -.-- .. .-.. .. -.- . -.-. .... . . ...') -eq 1 ]]; then echo -e "\e[32m\e[1mMorse Encode Working Successfully!"; else echo -e "\e[31m\e[1mMorse Encode not Working :("; fi) &

# morse_decode
(if [[ $(python C1pherH4x.py -s -d -ct '..-. .-.. .- --. ... .- -- ..- . .-.. -- --- .-. ... . .. ... -.-. --- --- .-.. -... -.-- - .... . .-- .- -.-- .. .-.. .. -.- . -.-. .... . . ...' | grep -Pzc '(?s)^FLAGSAMUELMORSEISCOOLBYTHEWAYILIKECHEES\n$') -eq 1 ]]; then echo -e "\e[32m\e[1mMorse Decode Working Successfully!"; else echo -e "\e[31m\e[1mMorse Decode not Working :("; fi) &

# xor_encode
(if [[ $(python C1pherH4x.py -e -pt '0xc4115' -c xor -k '0x4cf8' | grep -c '0xc0ded') -eq 1 ]]; then echo -e "\e[32m\e[1mXor Encode Working Successfully!"; else echo -e "\e[31m\e[1mXor Encode not Working :("; fi) &

# xor_decode
(if [[ $(python C1pherH4x.py -s -d -ct "q{vpln'bH_varHuebcrqxetrHOXEj" -c xor -ff 'flag{.*}' | grep -Pzc '(?s)^flag{y0u_Have_bruteforce_XOR}\n$') -eq 1 ]]; then echo -e "\e[32m\e[1mXor Decode Working Successfully!"; else echo -e "\e[31m\e[1mXor Decode not Working :("; fi) &

# vigenere_encode
(if [[ $(python C1pherH4x.py -s -e -pt "flag{CiphersAreAwesome}" -c vigenere -k 'blorpy' | grep -Pzc '(?s)^gwox{RgqssihYspOntqpxs}\n$') -eq 1 ]]; then echo -e "\e[32m\e[1mVigenere Encode Working Successfully!"; else echo -e "\e[31m\e[1mVigenere Encode not Working :("; fi) &

# vigenere_decode
(if [[ $(python C1pherH4x.py -s -d -ct "gwox{RgqssihYspOntqpxs}" -c vigenere -k "blorpy" -ff 'flag{.*}' | grep -Pzc '(?s)^flag{CiphersAreAwesome}\n$') -eq 1 ]]; then echo -e "\e[32m\e[1mVigenere Decode Working Successfully!"; else echo -e "\e[31m\e[1mVigenere Decode not Working :("; fi) &

sleep 0.1