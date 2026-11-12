from components.boards import HW1RISCVBoard
from components.processors import HW1TimingSimpleCPU
from components.processors import HW1MinorCPU
from components.cache_hierarchies import HW1MESITwoLevelCache
from components.memories import HW1DDR3_1600_8x8                        
from components.memories import HW1DDR3_2133_8x8                        
from components.memories import HW1LPDDR3_1600_1x32                     # 导入模型

from workloads.mat_mul_workload import MatMulWorkload                   # 导入工作负载
from gem5.simulate.simulator import Simulator                           # 导入模拟器/src/python/gem5

# 实例化模型对象
if __name__ == "__m5_main__":
    cpu = HW1MinorCPU()
    cache = HW1MESITwoLevelCache()
    memory = HW1DDR3_2133_8x8()
    board = HW1RISCVBoard(
        clk_freq="4GHz", processor=cpu, cache_hierarchy=cache, memory=memory
    )

    # 设置工作负载
    workload = MatMulWorkload(mat_size=224)  # 设置矩阵大小为224x224
    board.set_se_binary_workload(
        binary=workload["binary"],
        arguments=workload["arguments"],
    )

    #创建模拟器对象
    simulator = Simulator(board=board, full_system=False)
    simulator.run()
    print("Finished simulation.")
