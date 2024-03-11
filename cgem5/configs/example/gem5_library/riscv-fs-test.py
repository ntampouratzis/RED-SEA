import m5

from gem5.components.boards.riscv_board import RiscvBoard
from gem5.components.memory import SingleChannelDDR3_1600
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.cachehierarchies.classic.private_l1_private_l2_cache_hierarchy import (
    PrivateL1PrivateL2CacheHierarchy,
)
from gem5.components.processors.cpu_types import CPUTypes
from gem5.isas import ISA
from gem5.utils.requires import requires
from gem5.utils.override import overrides
from gem5.resources.resource import (
    Resource,
    CustomResource,
    DiskImageResource,
    FileResource,
)
from gem5.simulate.simulator import Simulator

# Run a check to ensure the right version of gem5 is being used.
requires(isa_required=ISA.RISCV)

# Setup the cache hierarchy.
# For classic, PrivateL1PrivateL2 and NoCache have been tested.
# For Ruby, MESI_Two_Level and MI_example have been tested.
cache_hierarchy = PrivateL1PrivateL2CacheHierarchy(
    l1d_size="32KiB", l1i_size="32KiB", l2_size="512KiB"
)

# Setup the system memory.
memory = SingleChannelDDR3_1600()

# Setup a single core Processor.
processor = SimpleProcessor(
    cpu_type=CPUTypes.ATOMIC, isa=ISA.RISCV, num_cores=16
)


class ModifiedRiscvBoard(RiscvBoard):
    @overrides(RiscvBoard)
    def get_default_kernel_args(self):
        return [
            "earlycon=uart8250,0x10000000",
            "console=uart8250,0x10000000",
            # "console=ttyS0",
            "lpj=7999923",
            "root=/dev/vda1",
            "rw init=/root/gem5_init.sh",
        ]


# Setup the board.
board = ModifiedRiscvBoard(
    clk_freq="1GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--bootloader", type=str, required=True)
parser.add_argument("--kernel", type=str, required=True)
parser.add_argument("--disk-image", type=str, required=True)

parser.add_argument("--cossim", action="store_true",
                      help="COSSIM distributed gem5 simulation.")

parser.add_argument("--nodeNum", action="store", type=int, dest="nodeNum", default=0,
                      help="Specify the number of node")

args = parser.parse_args()

board.platform.attachRISCVTerminal(args.cossim, args.nodeNum) #COSSIM

# Set the Full System workload.
board.set_kernel_disk_workload(
    bootloader=FileResource(args.bootloader),
    kernel=FileResource(args.kernel),
    disk_image=DiskImageResource(args.disk_image),
)

simulator = Simulator(board=board)
print("Beginning simulation!")
simulator.run()
print("exit 1")
simulator.run()
print("exit 2")
