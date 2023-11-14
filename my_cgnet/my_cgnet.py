import sys

sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks import *

inj_height = 13

arch = [
    to_head('..'),
    to_cor(),
    to_begin(),

    to_input('../images/ParamPlot_TMQ_data-2013-09-27-01-1_0_mirrored.png', name="image", width=12, height=8),

    to_Image("image_box", offset="(-0.6,0,0)", to="(image)", width=3, height=40, depth=60, opacity=0,
             caption="16 channels"),

    to_Node("node0", offset="(1.7,0,0)", to="(image_box-east)", radius=1, opacity=0.6),
    to_connection("image_box", "node0"),

    to_ConvConvConvPrelu(name="conv_b0", s_filer="I/2", n_filer=(32,32,32), offset="(1.5,0,0)", to="(0,0,0)",
        width=(1,1,1), height=28, depth=42, caption="Conv. layers"),
    to_connection("node0", "conv_b0"),

    to_Sum("sum1", offset="(2,0,0)", to="(conv_b0-east)", radius=1, opacity=0.6),
    to_connection("conv_b0", "sum1"),

    to_inject(of='node0', to='sum1', pos=inj_height),

    to_Node("node1", offset="(1.7,0,0)", to="(sum1-east)", radius=1, opacity=0.6),
    to_connection("sum1", "node1"),

    to_CGblock(name="cg_M", s_filer="I/4", offset="(2,0,0)", to="(node1-east)",
               number=3, width=1, height=20, depth=30, caption="3 CG blocks"),
    to_connection("node1", "cg_M"),

    to_Sum("sum2", offset="(2,0,0)", to="(cg_M-east)", radius=1, opacity=0.6),
    to_connection("cg_M", "sum2"),

    to_inject(of='node0', to='sum2', pos=inj_height),
    to_inject(of='node1', to='sum2', pos=inj_height),

    to_Node("node2", offset="(1.7,0,0)", to="(sum2-east)", radius=1, opacity=0.6),

    to_connection("sum2", "node2"),

    to_CGblock(name="cg_N1", s_filer="", offset="(2,0,0)", to="(node2-east)",
               number=2, width=1, height=14, depth=21, caption=""),
    to_connection("node2", "cg_N1"),

    to_CGblock(name="cg_N2", s_filer="I/8", offset="(2.4,0,0)", to="(cg_N1-east)",
               number=2, width=1, height=14, depth=21, caption=""),

    to_Image(name="cg_box", offset="(2,0,0)", to="(node2-east)", width=16, height=14, depth=21, opacity=0,
             caption="21 CG Blocks"),

    to_Node(name="dotdotdot", offset="(1.2,0,0)", to="(cg_N1-east)", radius=2, opacity=0, logo="..."),

    to_Sum("sum3", offset="(1.7,0,0)", to="(cg_N2-east)", radius=1, opacity=0.6),
    to_connection("cg_N2", "sum3"),
    to_inject(of='node2', to='sum3', pos=inj_height),

    to_ConvRelu("conv_end", "I/8", 3, offset="(1.7,0,0)", to="(sum3-east)",
                height=14, depth=21, width=2, caption="classify"),
    to_connection("sum3", "conv_end"),


    to_UpSample("upsample", offset="(4.4, 0, 0)", to="(conv_end-east)",
              width=1, height=40, depth=60, opacity=0.7, caption="upsample"),
    to_connection("conv_end", "upsample"),

    to_input('../images/data-2013-09-27-01-1_0_orig_mirrored.png', to="(upsample-east)", name="output",
             width=12, height=8),

    to_end(),
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()

