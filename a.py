import graphviz
import matplotlib.pyplot as plt
import numpy as np
import os

# --- 全局配置 ---
# 设置中文字体，确保在图中能正确显示中文
# 常见的选择: 'SimHei' (黑体), 'Microsoft YaHei' (微软雅黑), 'KaiTi' (楷体)
FONT_NAME = 'SimHei'

def set_chinese_font():
    """设置Matplotlib显示中文的字体"""
    plt.rcParams['font.sans-serif'] = [FONT_NAME]
    plt.rcParams['axes.unicode_minus'] = False # 解决负号显示为方块的问题

def check_font_availability():
    """检查字体是否可用，如果不可用则给出提示"""
    import matplotlib.font_manager as fm
    font_paths = fm.findSystemFonts(fontpaths=None, fontext='ttf')
    # 检查字体列表中是否包含我们需要的字体
    if not any(FONT_NAME.lower() in os.path.basename(p).lower() for p in font_paths):
        print(f"\n[警告]: 未在系统中找到 '{FONT_NAME}' 字体。")
        print("图表中的中文可能无法正常显示。请安装该字体或在代码中更换为您系统中已有的中文字体。")
        print("常见的备选字体有 'Microsoft YaHei', 'SimSun', 'KaiTi' 等。\n")
        return False
    return True

def generate_system_structure_diagram():
    """生成RFID系统结构示意图"""
    output_filename = 'system_structure'
    dot = graphviz.Digraph('RFID_System', comment='RFID System Structure')
    # 增加DPI设置以提高清晰度
    dot.attr(rankdir='LR', size='9,6', splines='ortho', dpi='300')
    dot.attr('node', shape='box', style='rounded,filled', fontname=FONT_NAME, fillcolor='#e6f7ff', color='#0066cc')
    dot.attr('edge', fontname=FONT_NAME, fontsize='10', color='#333333')

    dot.node('a', 'RFID电子标签\n(被检测目标)')
    dot.node('b', 'RFID读写器\n(智能检测传感器)')
    dot.node('c', '天线')
    dot.node('d', 'RFID中间件\n(数据预处理)')
    dot.node('e', '仓库管理系统(WMS)\n(数据应用端)')

    dot.edge('b', 'c', label=' 发射射频信号 ')
    dot.edge('c', 'a', label=' 激活标签 ')
    dot.edge('a', 'c', label=' 返回身份信息 ', dir='back')
    dot.edge('b', 'd', label=' 上传原始数据 ')
    dot.edge('d', 'e', label=' 传输有效信息 ')
    
    try:
        dot.render(output_filename, format='png', view=False, cleanup=True)
        print(f"成功: 已生成高清晰度图像 '{output_filename}.png'")
    except Exception as e:
        print(f"[错误] 生成 '{output_filename}.png' 失败: {e}")

def generate_workflow_diagram():
    """生成传统与RFID工作流程对比图"""
    output_filename = 'workflow_comparison'
    g = graphviz.Digraph('G', filename=f'{output_filename}.gv')
    # 增加DPI设置以提高清晰度
    g.attr(rankdir='TB', splines='ortho', fontname=FONT_NAME, label='仓储工作流程对比', fontsize='16', dpi='300')

    node_attr = {'shape': 'box', 'style': 'rounded', 'fontname': FONT_NAME}
    edge_attr = {'fontname': FONT_NAME, 'fontsize': '9'}

    with g.subgraph(name='cluster_0') as c:
        c.attr(label='传统条码流程', fontname=FONT_NAME, style='rounded', color='grey')
        c.node('t1', '货物到库', **node_attr)
        c.node('t2', '人工开箱', **node_attr)
        c.node('t3', '逐一扫描条码', **node_attr)
        c.node('t4', '数据手动录入', **node_attr)
        c.node('t5', '货物上架', **node_attr)
        c.edge('t1', 't2', **edge_attr)
        c.edge('t2', 't3', **edge_attr)
        c.edge('t3', 't4', **edge_attr)
        c.edge('t4', 't5', **edge_attr)

    with g.subgraph(name='cluster_1') as c:
        c.attr(label='RFID智能流程', fontname=FONT_NAME, style='rounded', color='blue')
        c.node('r1', '货物到库', **node_attr)
        c.node('r2', '整箱通过RFID通道门', **node_attr, fillcolor='#e6f7ff')
        c.node('r3', '批量自动识别', **node_attr, fillcolor='#e6f7ff')
        c.node('r4', '数据自动上传WMS', **node_attr, fillcolor='#e6f7ff')
        c.node('r5', '货物上架', **node_attr)
        c.edge('r1', 'r2', **edge_attr)
        c.edge('r2', 'r3', **edge_attr)
        c.edge('r3', 'r4', **edge_attr)
        c.edge('r4', 'r5', **edge_attr)

    try:
        g.render(output_filename, format='png', view=False, cleanup=True)
        print(f"成功: 已生成高清晰度图像 '{output_filename}.png'")
    except Exception as e:
        print(f"[错误] 生成 '{output_filename}.png' 失败: {e}")


def generate_efficiency_chart():
    """生成RFID与条码效率对比柱状图"""
    output_filename = 'efficiency_comparison'
    
    if not check_font_availability():
        return
    set_chinese_font()
    
    labels = ['入库处理时间', '出库准确率', '盘点耗时']
    barcode_data = [30, 98.5, 8]
    rfid_data = [5, 99.9, 0.5]

    x = np.arange(len(labels))
    width = 0.35

    # 增加图像尺寸和字体大小，以提高清晰度
    fig, ax1 = plt.subplots(figsize=(10, 6))
    plt.rcParams['font.size'] = 12

    ax2 = ax1.twinx()

    rects1 = ax1.bar(x[0] - width/2, barcode_data[0], width, label='条码', color='#ff9999')
    rects2 = ax1.bar(x[0] + width/2, rfid_data[0], width, label='RFID', color='#66b3ff')
    rects5 = ax1.bar(x[2] - width/2, barcode_data[2], width, color='#ff9999')
    rects6 = ax1.bar(x[2] + width/2, rfid_data[2], width, color='#66b3ff')

    rects3 = ax2.bar(x[1] - width/2, barcode_data[1], width, color='#ff9999')
    rects4 = ax2.bar(x[1] + width/2, rfid_data[1], width, color='#66b3ff')

    ax1.set_ylabel('时间 (分钟 / 小时)', fontsize=12)
    ax2.set_ylabel('准确率 (%)', fontsize=12)
    ax1.set_title('关键作业效率对比 (网络查询数据)', fontsize=16, pad=20)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, fontsize=12)
    
    ax1.set_ylim(0, max(barcode_data[0], barcode_data[2]) * 1.2)
    ax2.set_ylim(98, 100)

    lines, labels_l = ax1.get_legend_handles_labels()
    ax1.legend(lines, labels_l, loc='upper left', fontsize=11)
    
    ax1.bar_label(rects1, padding=3, fontsize=10)
    ax1.bar_label(rects2, padding=3, fontsize=10)
    ax2.bar_label(rects3, padding=3, fmt='%.1f%%', fontsize=10)
    ax2.bar_label(rects4, padding=3, fmt='%.1f%%', fontsize=10)
    ax1.bar_label(rects5, padding=3, fontsize=10)
    ax1.bar_label(rects6, padding=3, fontsize=10)

    fig.tight_layout()
    try:
        # 保存时指定DPI为300，这是印刷级别的清晰度
        plt.savefig(f"{output_filename}.png", dpi=300)
        print(f"成功: 已生成高清晰度图像 '{output_filename}.png'")
    except Exception as e:
        print(f"[错误] 生成 '{output_filename}.png' 失败: {e}")
    plt.close()


def main():
    """主函数，生成所有图表"""
    print("开始生成报告所需的高清晰度图表...")
    
    generate_system_structure_diagram()
    generate_workflow_diagram()
    generate_efficiency_chart()
    
    print("\n所有图表生成完毕。")
    print("如果遇到Graphviz错误，请确保已正确安装软件并将其添加到系统PATH。")

if __name__ == '__main__':
    main()

