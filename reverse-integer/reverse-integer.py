class Solution(object):
    def reverse(self, x):
        if x>2147483647 or x<-2147483648:
            return "0"
        
        data = str(x)
        flag_minus= False
        l = len(data);
        if data[0]=='-':
            flag_minus = True

        temp = ""
        if data=="0":
            return "0"
        else:
            sencond = True
            for i in range(l):
                if sencond:
                    if data[l-i-1]=="0" or data[l-i-1]=="-":
                        continue
                    else:
                        temp = temp+data[l-i-1]
                        sencond = False
                else:
                    if  data[l-i-1]=="-":
                        continue;
                    else:
                        temp = temp+data[l-i-1]
            
            
            if flag_minus:
                data =  "-"+temp
                x = int(data)
                if x>2147483647 or x<-2147483648:
                    return "0"
                else:
                    return x;
            else:
                x = int(temp)
                if x>2147483647 or x<-2147483648:
                    return "0"
                else:
                    return x;