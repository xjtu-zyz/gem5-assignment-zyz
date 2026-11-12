from components.boards import HW0RISCVBoard
from components.processors import HW0TimingSimpleCPU
from components.cache_hierarchies import HW0MESITwoLevelCache
from components.memories import HW0DDR3_1600_8x8                        # 导入模型

from workloads.hello_world_workload import HelloWorldWorkload           # 导入工作负载
from gem5.simulate.simulator import Simulator                           # 导入模拟器/src/python/gem5

# 实例化模型对象
if __name__ == "__m5_main__":
    cpu = HW0TimingSimpleCPU()
    cache = HW0MESITwoLevelCache()
    memory = HW0DDR3_1600_8x8()
    board = HW0RISCVBoard(
        clk_freq="2GHz", processor=cpu, cache_hierarchy=cache, memory=memory
    )

    # 设置工作负载
    workload = HelloWorldWorkload()
    board.set_se_binary_workload(workload)


    #创建模拟器对象
    simulator = Simulator(board=board, full_system=False)
    simulator.run()
    print("Finished simulation.")
