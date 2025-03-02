<template>
  <div class="home">
    <transition name="fade" mode="out-in">
      <dv-border-box-10>
        <div class="naca">
          <div class="index-header" style="margin-top: 5px">
          </div>

          <div class="index-content">
              <br>
             <div style="text-align: center; font-size: 28px; color: #FFA500; margin-top: 20px;">内 核 漏 洞 检 测</div>
            <div class="left">
                <div style="font-size: 20px; font-weight: bold; display: flex; justify-content: space-between; align-items: center;">
                    <div style="padding: 10px; margin-bottom: 10px; background-color: rgba(63, 150, 165, 0.1);">
                      <span style="font-size: 24px; color: #FF5733;">检测时间：</span>
                      <span style="font-size: 24px; color: #00FF00;">{{ checkTime }}</span>
                    </div>
                    <div style="padding: 10px; margin-bottom: 10px; background-color: rgba(63, 150, 165, 0.1);">
                      <span style="font-size: 24px; color: #FF5733;">主机名称：</span>
                      <span style="font-size: 24px; color: #00FF00;">{{ hostname }}</span>
                    </div>
                    <div style="padding: 10px; margin-bottom: 10px; background-color: rgba(63, 150, 165, 0.1);">
                      <span style="font-size: 24px; color: #FF5733;">扫描类型：</span>
                      <span style="font-size: 24px; color: #00FF00;">{{ scanType }}</span>
                    </div>
                    <div style="padding: 10px; background-color: rgba(63, 150, 165, 0.1); margin-top: -10px;">
                      <span style="font-size: 24px; color: #FF5733;">安全评分：</span>
                      <span style="font-size: 24px; color: #00FF00;">{{ score }}</span>
                    </div>
                    <a href="http://152.136.142.183:39010/nbugrepair" target="_blank" style="padding: 10px 20px; background-color: #4CAF50; color: white; border-radius: 5px; margin-top: -10px;">修复漏洞</a>
                  </div>
              <dv-border-box-10>
                  <!-- 基线检查结果表格 -->
                  <table class="baseline-result">
                    <thead>
                      <tr>
                        <th>序号</th>
                        <th>漏洞名称</th>
                        <th>是否存在</th>
                        <th>解决方案</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(item, index) in bugResults" :key="index">
                        <td>{{ index + 1 }}</td>
                        <td>{{ item.name }}</td> 
                        <td>{{item.CheckResult}}</td>
                        <td>
                          <a :href="item.solution" target="_blank" style="font-size: 18px; color: inherit;">
                          <span v-if="item.solution.length > 50">
                            {{ item.solution.slice(0, 50) }}
                            <br>
                            {{ item.solution.slice(50) }}
                          </span>
                          <span v-else>{{ item.solution }}</span>
                          </a>
                        </td> 
                      </tr>
                    </tbody>
                  </table>
                  <dv-scroll-ranking-board :config="config5" style="width:871px;height:4px"/>
              </dv-border-box-10>
             <div style="text-align: center; font-size: 28px; color: #FFA500; margin-top: 20px;">系 统 漏 洞 检 测</div>
             <br>
             <div style="font-size: 20px; font-weight: bold; display: flex; justify-content: space-between; align-items: center;">
                    <div style="padding: 10px; margin-bottom: 10px; background-color: rgba(63, 150, 165, 0.1);">
                      <span style="font-size: 24px; color: #FF5733;">检测时间：</span>
                      <span style="font-size: 24px; color: #00FF00;">{{ checkTime1 }}</span>
                    </div>
                    <div style="padding: 10px; margin-bottom: 10px; background-color: rgba(63, 150, 165, 0.1);">
                      <span style="font-size: 24px; color: #FF5733;">主机名称：</span>
                      <span style="font-size: 24px; color: #00FF00;">{{ hostname1 }}</span>
                    </div>
                    <div style="padding: 10px; margin-bottom: 10px; background-color: rgba(63, 150, 165, 0.1);">
                      <span style="font-size: 24px; color: #FF5733;">扫描类型：</span>
                      <span style="font-size: 24px; color: #00FF00;">{{ scanType1 }}</span>
                    </div>
                    <div style="padding: 10px; background-color: rgba(63, 150, 165, 0.1); margin-top: -10px;">
                      <span style="font-size: 24px; color: #FF5733;">安全评分：</span>
                      <span style="font-size: 24px; color: #00FF00;">{{ score1 }}</span>
                    </div>
                    <a href="http://152.136.142.183:39010/xbugrepair" target="_blank" style="padding: 10px 20px; background-color: #4CAF50; color: white; border-radius: 5px; margin-top: -10px;">修复漏洞</a>
                  </div>
             <dv-border-box-10>
                  <!-- 基线检查结果表格 -->
                  <table class="baseline-result">
                    <thead>
                      <tr>
                        <th>序号</th>
                        <th>漏洞名称</th>
                        <th>是否存在</th>
                        <th>解决方案</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(item, index) in bugResults1" :key="index">
                        <td>{{ index + 1 }}</td>
                        <td>{{ item.name }}</td>
                        <td>{{item.checkResult}} <!-- 这里修改为小写的 checkResult -->
                        </td>
                        <td><a :href="item.solution" target="_blank" style="font-size: 18px; color: inherit;">{{ item.solution }}</a></td>  
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

// 定义计算漏洞风险得分的函数
function calculateRiskScore(bugResults) {
  let criticalCount = 0;
  let highCount = 0;
  let mediumCount = 0;
  let lowCount = 0;

  bugResults.forEach(item => {
    const checkResult = item[Object.keys(item)[0]].CheckResult;
    if (checkResult === 0) {
      if (Object.keys(item)[0].startsWith('CVE-') || Object.keys(item)[0].startsWith('KVE-')) {
        if (Object.keys(item)[0].includes('-Critical')) {
          criticalCount++;
        } else if (Object.keys(item)[0].includes('-High')) {
          highCount++;
        } else if (Object.keys(item)[0].includes('-Medium')) {
          mediumCount++;
        } else {
          lowCount++;
        }
      }
    }
  });

  const totalScore = (criticalCount * 10) + (highCount * 5) + (mediumCount * 2) + lowCount;

  if (totalScore >= 30) {
    return 0;
  } else if (totalScore >= 20) {
    return 25;
  } else if (totalScore >= 10) {
    return 50;
  } else {
    return 75;
  }
}

export default {
  data() {
    return {
      bugResults: [],
      checkTime: '',
      hostname: '',
      scanType: '',
      score: 0,
      
      bugResults1: [],
      checkTime1: '',
      hostname1: '',
      scanType1: '',
      score1: 0
    };
  },
  created() {
    axios.get('/api/nbug')
 .then(response => {
            const data = response.data;
            this.bugResults = data.slice(2).map(item => ({
                name: Object.keys(item)[0],
                CheckResult: item[Object.keys(item)[0]].CheckResult === 0? '否' : '是',
                solution: item[Object.keys(item)[0]].solution
            }));
    
            this.checkTime = data[0].CheckTime;
            this.hostname = data[1].Hostname;
            this.scanType = 'Kernel';
            this.score = calculateRiskScore(this.bugResults);   // 使用计算风险分数的函数来设置内核漏洞分数
          })
 .catch(error => {
            console.error('Error fetching kernel bug data:', error);
          });

    axios.get('/api/xbug')
.then(response => {
        const systemData = response.data;
        this.bugResults1 = systemData.slice(2).map(item => ({
            name: Object.keys(item)[0],
            checkResult: item[Object.keys(item)[0]].CheckResult === 0? '否' : '是', // 这里修改为小写的 checkResult
            solution: item[Object.keys(item)[0]].solution
        }));
        this.checkTime1 = systemData[0].CheckTime;
        this.hostname1 = systemData[1].Hostname;
        this.scanType1 = 'System';
        this.score1 = calculateRiskScore(this.bugResults1);   // 使用计算风险分数的函数来设置系统漏洞分数
        console.log('Fetched system bug data:', systemData); // 增加调试输出
        console.log('Mapped system bug results:', this.bugResults1); // 增加调试输出
      })
.catch(error => {
        console.error('Error fetching system bug data:', error);
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

.baseline-result th:nth-child(1) {  
  font-size: 20px;
  background-color: rgba(63, 150, 165, 0.1) ;
}

.baseline-result th:nth-child(2) {  
  font-size: 20px;
  background-color: rgba(63, 150, 165, 0.1) ;
}

.baseline-result th:nth-child(3) {  
  font-size: 20px;
  background-color: rgba(63, 150, 165, 0.1) ;
}
.baseline-result th:nth-child(4) {  
  font-size: 20px;
  background-color: rgba(63, 150, 165, 0.1) ;
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
  Color: White;
  border: none;
  Border-radius: 8px; 
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