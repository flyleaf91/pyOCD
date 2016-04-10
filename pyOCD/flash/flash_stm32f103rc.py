"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from flash import Flash


"""
flash_algo RAW Demo
"""
flash_algo_raw = { 'load_address' : 0x20000000,
               'instructions' : [
                                  0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
                                  0x49384839, 0x49396041, 0x20006041, 0x49364770, 0x60c82034, 0x47702000, 0x47702000, 0xb5004a32,
                                  0x06006910, 0xf7ffd501, 0x68d0ffeb, 0xd1fc07c0, 0xf0406910, 0x61100004, 0xf0406910, 0x61100040,
                                  0x07c068d0, 0x6910d1fc, 0x0004f020, 0x20006110, 0x4a25bd00, 0x4603b500, 0x06006910, 0xf7ffd501,
                                  0x68d1ffcf, 0xd1fc07c9, 0xf0406910, 0x61100002, 0x69106153, 0x0040f040, 0x68d06110, 0xd1fc07c0,
                                  0xf0206910, 0x61100002, 0xbd002000, 0x4d16b570, 0x460e4603, 0x24006928, 0xd5010600, 0xffb0f7ff,
                                  0x07c068e8, 0xe014d1fc, 0x0001f040, 0x88106128, 0x68e88018, 0xd1fc07c0, 0x88198810, 0xd0054288,
                                  0xf0206928, 0x61280001, 0xbd702001, 0x1c9b1c92, 0x69281c64, 0x0f56ebb4, 0xf020d3e6, 0x61280001,
                                  0xbd702000, 0x45670123, 0x40022000, 0xcdef89ab, 0x00000000,
                                ],
               'pc_init'          : 0x2000002F,
               'pc_eraseAll'      : 0x2000003D,
               'pc_erase_sector'  : 0x20000073,
               'pc_program_page'  : 0x200000AD,
               'static_base'      : 0x20000200,
               'begin_data'       : 0x20001000, # Analyzer uses a max of 1 KB data (256 pages * 4 bytes / page)
               'page_buffers'    : [0x20001000, 0x20001800],   # Enable double buffering
               'begin_stack'      : 0x20002800,
               'min_program_length' : 2,
               'analyzer_supported' : True,
               'analyzer_address' : 0x20003000 # Analyzer 0x20003000..0x20003600
              };


"""
flash_algo_pack RAW bin ,not exchange LOW HIGH
"""
flash_algo_pack_bin = { 'load_address' : 0x20000000,
               'instructions' : [
0x4603b510, 0x04c00cd8, 0x444c4c45, 0x20006020,
0x60204c44, 0x60604844, 0x60604844, 0x69c04620,
0x0f04f010, 0xf245d108, 0x4c415055, 0x20066020,
0xf6406060, 0x60a070ff, 0xbd102000, 0x48394601,
0xf0406900, 0x4a370080, 0x20006110, 0x48354770,
0xf0406900, 0x49330004, 0x46086108, 0xf0406900,
0x61080040, 0xf64ae003, 0x493120aa, 0x482d6008,
0xf01068c0, 0xd1f60f01, 0x6900482a, 0x0004f020,
0x61084928, 0x47702000, 0x48264601, 0xf0406900,
0x4a240002, 0x46106110, 0x69006141, 0x0040f040,
0xe0036110, 0x20aaf64a, 0x60104a21, 0x68c0481d,
0x0f01f010, 0x481bd1f6, 0xf0206900, 0x4a190002,
0x20006110, 0xb5104770, 0x1c484603, 0x0101f020,
0x4814e022, 0xf0406900, 0x4c120001, 0x88106120,
0xbf008018, 0x68c0480f, 0x0f01f010, 0x480dd1fa,
0xf0206900, 0x4c0b0001, 0x46206120, 0xf01068c0,
0xd0060f14, 0x68c04620, 0x0014f040, 0x200160e0,
0x1c9bbd10, 0x1e891c92, 0xd1da2900, 0xe7f72000,
0x00000004, 0x40022000, 0x45670123, 0xcdef89ab,
0x40003000, 0x00000000, 0x00000000, 
                                ],
               'pc_init'          : 0x20000000,
               'pc_eraseAll'      : 0x2000004e,
               'pc_erase_sector'  : 0x20000088,
               'pc_program_page'  : 0x200000c6,
               'static_base'      : 0x20000134,
               'begin_data'       : 0x20001000, # Analyzer uses a max of 1 KB data (256 pages * 4 bytes / page)
               'page_buffers'    : [0x20001000, 0x20001800],   # Enable double buffering
               'begin_stack'      : 0x20002800,
               'min_program_length' : 2,
               'analyzer_supported' : False,
               'analyzer_address' : 0x20003000 # Analyzer 0x20003000..0x20003600
              };

"""
flash_algo_pack bin,exchange LOW HIGH
"""
flash_algo_pack_leh = { 'load_address' : 0x20000000,
               'instructions' : [
                                  0x034610b5, 0xc004d80c, 0x4c44454c, 0x00202060,0x2060444c, 0x60604448, 0x60604448, 0xc0692046,
                                  0x040f10f0, 0x45f208d1, 0x414c5550, 0x06202060,0x40f66060, 0xa060ff70, 0x10bd0020, 0x39480146,
                                  0x40f00069, 0x374a8000, 0x00201061, 0x35487047,0x40f00069, 0x33490400, 0x08460861, 0x40f00069,
                                  0x08614000, 0x4af603e0, 0x3149aa20, 0x2d480860,0x10f0c068, 0xf6d1010f, 0x00692a48, 0x040020f0,
                                  0x08612849, 0x70470020, 0x26480146, 0x40f00069,0x244a0200, 0x10461061, 0x00694161, 0x400040f0,
                                  0x03e01061, 0xaa204af6, 0x1060214a, 0xc0681d48,0x010f10f0, 0x1b48f6d1, 0x20f00069, 0x194a0200,
                                  0x00201061, 0x10b57047, 0x481c0346, 0x010120f0,0x144822e0, 0x40f00069, 0x124c0100, 0x10882061,
                                  0x00bf1880, 0xc0680f48, 0x010f10f0, 0x0d48fad1,0x20f00069, 0x0b4c0100, 0x20462061, 0x10f0c068,
                                  0x06d0140f, 0xc0682046, 0x140040f0, 0x0120e060,0x9b1c10bd, 0x891e921c, 0xdad10029, 0xf7e70020,
                                  0x00000400, 0x02400020, 0x67452301, 0xefcdab89,0x00400030, 0x00000000, 0x00000000, 
                                ],
               'pc_init'          : 0x20000001,
               'pc_eraseAll'      : 0x2000004f,
               'pc_erase_sector'  : 0x20000089,
               'pc_program_page'  : 0x200000c7,
               'static_base'      : 0x20000134,
               'begin_data'       : 0x20001000, # Analyzer uses a max of 1 KB data (256 pages * 4 bytes / page)
               'page_buffers'    : [0x20001000, 0x20001800],   # Enable double buffering
               'begin_stack'      : 0x20002800,
               'min_program_length' : 2,
               'analyzer_supported' : False,
               'analyzer_address' : 0x20003000 # Analyzer 0x20003000..0x20003600
              };              

flash_algo = flash_algo_pack_bin

class Flash_stm32f103rc(Flash):

    def __init__(self, target):
        super(Flash_stm32f103rc, self).__init__(target, flash_algo)


