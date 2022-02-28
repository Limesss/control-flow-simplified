from idaapi import *
import idc
import os
import idautils
class Anaysis_Block(plugin_t):  
    flags=0
    wanted_name="Anaysis Block"  
    wanted_hotkey="F1"  
    comment="Anaysis Block"  
    help="Something helpful"  
    def init(self):  
        pass
        return PLUGIN_OK  
    def term(self):  
        pass
    def run(self,arg):  
        target=0x40fb1e
        ea = idc.get_screen_ea()
        f=get_func(ea)
        fc=FlowChart(f, flags=FC_PREDS)
        stack=[]
        trace=[]
        addr_list=[]
        for block in fc:
            stack.append(block)
        for block in stack[::-1]:
            if block.start_ea==target:
                addr = block.preds()
                for i in addr:
                    target=i.start_ea
                trace.append(block)
        for i in trace[::-1]:
            cur_addr=i.start_ea 
            addr_list.append(range(i.start_ea,i.end_ea))
            print("----------BLOCK   sub_%x--------------"%(cur_addr))
            while cur_addr<= i.end_ea:
                print("0x%x %s" % (cur_addr, idc.generate_disasm_line(cur_addr, 0)))
                cur_addr = idc.next_head(cur_addr, i.end_ea)
        print("END")
        print(addr_list)
        start_addr=0x4013e9
        while start_addr<=0x41038e:
            exis=0
            for i in addr_list:
                if start_addr  in i:
                    exis=1
                    break
            if exis!=1:
                idc.patch_byte(start_addr,0x90)
            start_addr=start_addr+1
            
def PLUGIN_ENTRY():  
    return Anaysis_Block()  
