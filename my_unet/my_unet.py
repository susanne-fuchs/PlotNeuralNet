
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [ 
    to_head('..'), 
    to_cor(),
    to_begin(),
    
    #input
    to_input('../images/ParamPlot_TMQ_data-2013-09-27-01-1_0_mirrored.png', name="image", width=12, height=8),
    to_Image("image_box", offset="(-0.6,0,0)", to="(image)", width=3, height=40, depth=60, opacity=0,
             caption="16 channels"),

    to_Conv("conv_b0", "I", 16, offset="(2,0,0)", to="(image_box-east)", height=40, depth=60, width=2 ),

    to_connection("image_box", "conv_b0"),

    *block_Pool2Conv(name='b1', botton='conv_b0', top='ccr_b1', s_filer="I/2", n_filer=32, offset="(2,0,0)",
                     size=(28, 42, 3.5), opacity=0.9),
    *block_Pool2Conv(name='b2', botton='ccr_b1', top='ccr_b2', s_filer="I/4", n_filer=64, offset="(2,0,0)",
                     size=(20, 30, 4.5), opacity=0.9),
    *block_Pool2Conv(name='b3', botton='ccr_b2', top='ccr_b3', s_filer="I/8", n_filer=128, offset="(2,0,0)",
                     size=(14, 21, 5.5), opacity=0.9),
    *block_Pool2Conv(name='b4', botton='ccr_b3', top='ccr_b4', s_filer="I/16", n_filer=256, offset="(2,0,0)",
                     size=(10, 15, 6.5), opacity=0.9),

    *block_Decode(name="d1", botton="ccr_b4", top='ccr_d1', s_filer="I/8", n_filer=128, offset="(2.1,0,0)",
                  size=(14, 21, 5.5), opacity=0.5),

    to_skip(of='ccr_b3', to='transpose_d1', pos=1.25),

    *block_Decode(name="d2", botton="ccr_d1", top='ccr_d2', s_filer="I/4", n_filer=64, offset="(2.1,0,0)",
                  size=(20, 30, 4.5), opacity=0.5),
    to_skip(of='ccr_b2', to='transpose_d2', pos=1.25),

    *block_Decode(name="d3", botton="ccr_d2", top='ccr_d3', s_filer="I/2", n_filer=32, offset="(2.1,0,0)",
                  size=(28, 42, 3.5), opacity=0.5),
    to_skip(of='ccr_b1', to='transpose_d3', pos=1.25),

    *block_Decode(name="d4", botton="ccr_d3", top='ccr_d4', s_filer="I", n_filer=16, offset="(2.1,0,0)",
                  size=(40, 60, 2), opacity=0.5),
    to_skip(of='conv_b0', to='transpose_d4', pos=1.25),

    to_Conv("conv_out", "I", 16, offset="(2,0,0)", to="(ccr_d4-east)", height=40, depth=60, width=2 ),
    to_connection( "ccr_d4", "conv_out"),

    to_input('../images/data-2013-09-27-01-1_0_orig_mirrored.png', to="(conv_out-east)", name="output",
             width=12, height=8),

    to_end(),
    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    
