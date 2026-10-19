class Solution:
    def compress(self, chars: list[str]) -> int:
        length = len(chars)
        read = 1
        write = 0

        while read < length:
            count = 1

            while read < length and chars[read] == chars[read-1]:
                if count == 1:
                    write = read

                count += 1
                read += 1
            
            else:
                if count > 1:
                    sc = str(count)
                    if count > 9:                        
                        numlist = list(sc)

                        for n in numlist:
                            chars[write] = n
                            write += 1
                        write -= 1
                    
                    else:
                        chars[write] = sc


                    while write+1 < read:
                        chars.pop(write+1)
                        read -= 1


                read += 1
                count = 1
                length = len(chars)

       
                        
        return len(chars)