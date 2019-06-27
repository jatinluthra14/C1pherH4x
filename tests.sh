#!/bin/bash

# bacon_decode
(if [[ $(python C1pherH4x.py -d -s -ct 'ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB' | grep -c 'ILOUEBACONDONTYOU') -eq 1 ]]; then echo -e "\e[32m\e[1mBacon Decode Working Successfully!"; else echo -e "\e[31m\e[1mBacon Decode not Working :("; fi) &

# base64_decode
(if [[ $(python C1pherH4x.py -d -s -ct "Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9" -ff "CTF{.*}" | grep -Pzc '(?s)^CTF{FlaggyWaggyRaggy}\n$') -eq 1 ]]; then echo -e "\e[32m\e[1mBase64 Decode Working Successfully!"; else echo -e "\e[31m\e[1mBase64 Decode not Working :("; fi) &

# morse_decode
(if [[ $(python C1pherH4x.py -s -d -ct '..-. .-.. .- --. ... .- -- ..- . .-.. -- --- .-. ... . .. ... -.-. --- --- .-.. -... -.-- - .... . .-- .- -.-- .. .-.. .. -.- . -.-. .... . . ...' | grep -Pzc '(?s)^FLAGSAMUELMORSEISCOOLBYTHEWAYILIKECHEES\n$') -eq 1 ]]; then echo -e "\e[32m\e[1mMorse Decode Working Successfully!"; else echo -e "\e[31m\e[1mMorse Decode not Working :("; fi) &

# xor_decode
(if [[ $(python C1pherH4x.py -s -d -ct "q{vpln'bH_varHuebcrqxetrHOXEj" -c xor -ff 'flag{.*}' | grep -Pzc '(?s)^flag{y0u_Have_bruteforce_XOR}\n$') -eq 1 ]]; then echo -e "\e[32m\e[1mXor Decode Working Successfully!"; else echo -e "\e[31m\e[1mXor Decode not Working :("; fi) &

sleep 0.1