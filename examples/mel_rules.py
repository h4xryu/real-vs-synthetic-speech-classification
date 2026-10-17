"""멜 계수와 청각 특징의 크기만 보고 라벨을 고른다.

c[0]부터 c[25]까지는 낮은 주파수에서 높은 주파수로 가는 로그 멜 에너지다.
c[26] 스펙트럼 중심 (kHz)
c[27] 스펙트럼 평탄도
c[28] RMS (dB)
c[29] 영교차율
c[30] 스펙트럼 롤오프 (kHz)
c[31] 낮은 멜 대역 에너지 비율
c[32] 높은 멜 대역 에너지 비율
"""

def predict(c):
    if c[0] <= -5.5821:
        if c[1] <= -3.0820:
            if c[2] <= -2.1101:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
            elif c[2] <= -0.2528:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
            else:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
        elif c[1] <= -0.5791:
            if c[2] <= -2.1101:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
            elif c[2] <= -0.2528:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
            else:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
        else:
            if c[2] <= -2.1101:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
            elif c[2] <= -0.2528:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
            else:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
    elif c[0] <= -3.1597:
        if c[1] <= -3.0820:
            if c[2] <= -2.1101:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
            elif c[2] <= -0.2528:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
            else:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
        elif c[1] <= -0.5791:
            if c[2] <= -2.1101:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
            elif c[2] <= -0.2528:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        else:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        else:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
            else:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
        else:
            if c[2] <= -2.1101:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
            elif c[2] <= -0.2528:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
            else:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
    else:
        if c[1] <= -3.0820:
            if c[2] <= -2.1101:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
            elif c[2] <= -0.2528:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
            else:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
        elif c[1] <= -0.5791:
            if c[2] <= -2.1101:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
            elif c[2] <= -0.2528:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
                        else:
                            if c[6] <= -3.8238:
                                return "sovits"
                            elif c[6] <= -2.0955:
                                return "sovits"
                            else:
                                return "sovits"
            else:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
        else:
            if c[2] <= -2.1101:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
            elif c[2] <= -0.2528:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        else:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        else:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        else:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        else:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        else:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                        else:
                            if c[6] <= -3.8238:
                                return "original"
                            elif c[6] <= -2.0955:
                                return "original"
                            else:
                                return "original"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
                        else:
                            if c[6] <= -3.8238:
                                return "voice_conversion"
                            elif c[6] <= -2.0955:
                                return "voice_conversion"
                            else:
                                return "voice_conversion"
            else:
                if c[3] <= -2.1336:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                elif c[3] <= -0.6840:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                else:
                    if c[4] <= -2.0927:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    elif c[4] <= -0.5508:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                    else:
                        if c[5] <= -2.6217:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        elif c[5] <= -0.9825:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
                        else:
                            if c[6] <= -3.8238:
                                return "TTS"
                            elif c[6] <= -2.0955:
                                return "TTS"
                            else:
                                return "TTS"
