
<template>
  <div class="home">
    <transition name="fade" mode="out-in">
      <dv-border-box-10>
        <div class="naca">
          <div class="index-header" style="margin-top: 5px">
          </div>

          <div class="index-content">
            <div class="left">
                <div style="font-size: 20px; font-weight: bold; display: flex; justify-content: space-between; align-items: center;">
                    <div style="padding: 10px; margin-bottom: 10px; background-color: rgba(63, 150, 165, 0.1);">
                      <span style="font-size: 24px; color: #FF5733;">检测时间：</span>
                      <span style="font-size: 24px; color: #00FF00;">{{ checkTime }}</span>  <!-- 更改检查时间值的颜色为绿色 -->
                    </div>
                    <div style="padding: 10px; margin-bottom: 10px; background-color: rgba(63, 150, 165, 0.1);">
                      <span style="font-size: 24px; color: #FF5733;">主机名称：</span>
                      <span style="font-size: 24px; color: #FF00FF;">{{ hostname }}</span>  <!-- 更改主机名称值的颜色为紫色 -->
                    </div>
                    <div style="padding: 10px; margin-bottom: 10px; background-color: rgba(63, 150, 165, 0.1);">
                      <span style="font-size: 24px; color: #FF5733;">扫描类型：</span>
                      <span style="font-size: 24px; color: #FFA500;">{{ scanType }}</span>  <!-- 更改扫描类型值的颜色为橙色 -->
                    </div>
                    <div style="padding: 10px; background-color: rgba(63, 150, 165, 0.1); margin-top: -10px;">
                      <span style="font-size: 24px; color: #FF5733;">检测评分：</span>
                      <span style="font-size: 24px; color: #0000FF;">{{ score }}</span>  <!-- 更改检测评分值的颜色为蓝色 -->
                    </div>
                  </div>
              <dv-border-box-10>
                  
                  <!-- 基线检查结果表格 -->
                  <table class="baseline-result">
                    <thead>
                      <tr>
                        <th>序号</th>
                        <th>所属</th>
                        <th>建议</th>
                        <th>站点信息名称</th>
                        <th style="width: 200px;">结果</th> 
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(item, index) in baselineResults" :key="item.Id">
                        <td>{{ index + 1 }}</td>
                        <td>{{ item.Belong }}</td>
                        <td>{{ item.Advice }}</td>
                        <td>{{ item.SiteInfo_Name }}</td>
                        <td>{{ item.Result }}</td>
                      </tr>
                    </tbody>
                  </table>
                  <dv-scroll-ranking-board :config="config5" style="width:871px;height:4px"/>
              </dv-border-box-10>
            </div>
          </div>
        </div>
      </dv-border-box-10>
    </transition>
  </div>
</template>

<script>
import axios from 'axios';
import Baselinerepair from './baselinerepair.vue';

const routes = [
  // 其他已有的路由配置...
  {
    path: '/baselinerepair',
    name: 'Baselinerepair',
    component: Baselinerepair
  }
];

export default {
  data() {
    return {
      baselineResults: [],
      checkTime: '',
      hostname: '',
      scanType: '',
      score: 0 // 初始化为 0，根据您的规则计算后更新
    };
  },
  created() {
    axios.get('/api/get_baseline_results')
 .then(response => {
        this.baselineResults = response.data[0].ScanProject;
        this.checkTime = response.data[0].CheckTime;
        this.hostname = response.data[0].Hostname;
        this.scanType = response.data[0].ScanType;
        // 计算检测评分，例如根据完成的检查项数量和建议调整的数量
        let totalItems = this.baselineResults.length;
        let needAdjustItems = this.baselineResults.filter(item => item.Advice!== 'No advice').length;
        this.score = Math.round((totalItems - needAdjustItems) / totalItems * 100);
      })
 .catch(error => {
        console.error('Error fetching baseline results:', error);
      });
  },
};
</script>


<style lang="less" scoped>
.baseline-result {
  margin-top: 10px; 
  margin-bottom: 5px; 
  width: 100%;
  border-collapse: collapse;
}

.baseline-result th,
.baseline-result td {
  border-bottom: 1px solid rgba(255, 255, 255, 0.1); 
  padding: 14px 10px; 
  text-align: left;
  color: #e0e0e0; 
  font-size: 16px; 
}

.baseline-result th:nth-child(1) {  // 序号
  font-size: 20px;
  background-color: rgba(63, 150, 165, 0.1) ;
}

.baseline-result th:nth-child(2) {  // 所属
  font-size: 20px;
  background-color: rgba(63, 150, 165, 0.1) ;
}

.baseline-result th:nth-child(3) {  // 建议
  font-size: 20px;
  background-color: rgba(63, 150, 165, 0.1) ;
}

.baseline-result th:nth-child(4) {  // 站点信息名称
  font-size: 20px;
  background-color: rgba(63, 150, 165, 0.1) ;
}

.baseline-result th:nth-child(5) {  // 结果
  font-size: 20px;
  background-color: rgba(63, 150, 165, 0.1) ;
  width: 200px; 
}

.baseline-result th {
  font-weight: 700; 
  text-transform: uppercase; 
  color: #bcbcbc; 
}

.baseline-result tr:hover {
  background-color: rgba(255, 255, 255, 0.03); 
}

.controls {
  margin: 20px;
  display: flex;
  justify-content: space-around;
}

.control-button {
  padding: 20px 20px;
  margin-top: 25px;
  background-color: #3f96a5;
  Color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
/* dv-scroll-ranking-board 组件样式调整 */
.dv-scroll-ranking-board {
  height: auto;
  margin: 20px 0;
}
.scores {
  margin: 20px;
  display: flex;
  justify-content: space-around;
}

.score-item {
  color: #3f96a5;
  font-size: 18px;
  font-weight: bold;
}

.score {
  color: #ffcc00;
  font-size: 24px;
}
/* 添加样式以美化按钮和评分显示 */
.controls {
  margin: 30px 20px; 
  display: flex;
  justify-content: space-around;
}

.control-button {
  padding: 12px 24px; 
  background-color: #3f96a5;
  Color: white;
  border: none;
  border-radius: 8px; 
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease; 
}
.control-button:hover {
  background-color: #2f7c8c; 
}
.scores {
  margin: 20px;
  display: flex;
  justify-content: space-around;
}

.title {
  font-size: 28px; 
  font-weight: 700; 
  text-align: center;
  margin-bottom: 1px;
  color: #e0e0e0; 
  letter-spacing: 1px; 
}

.left {
  padding: 20px;
  background-color: transparent; 
}
.right {
  padding: 20px;
  background-color: transparent; 
}
.score-item {
  color: #3f96a5;
  font-size: 20px;
  font-weight: bold;
  margin: 0 10px;
}

.score {
  color: #ffcc00;
  font-size: 28px;
}

</style>