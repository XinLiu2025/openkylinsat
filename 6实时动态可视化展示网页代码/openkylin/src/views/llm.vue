<template>  
  <div id="app">  
    <header>  
      <h1>将 AI 大模型技术，深度融入操作系统的安全检测领域</h1>  
    </header> 
    <img src="../assets/点击此处进入OS智能体(1).png" alt="" class="analysis-image" width="1440" height="630" @click="redirectToUrl"/>
  </div>  
</template> 

<script>  
export default {  
  data() {  
    return {  
     
    };  
  },  
  methods: {  
    redirectToUrl() {
      window.location.href = 'https://chatglm.cn/main/gdetail/66bad154a263443091256cb3';
    }
  }  
};  
</script>  

<style scoped>  
/* 这里是组件的样式，可以使用scoped属性确保样式只作用于当前组件 */  
header {  
  background-color: #0b50f0;  
  color: white;  
  padding: 15px;  
  text-align: center;  
}  

.news-container {  
  height: 35rem;
  margin: 20px; 
  /*width: 100%; */
  padding: 20px;  
  border: 1px solid #898686;  
  border-radius: 5px; 
  /* background-color: #050A31;  */
}  

.news-item {  
  margin-bottom: 20px;  
}  

.news-item h2 {  
  margin: 5px;  
  color: rgb(243, 243, 243);
  font-size:200%;
}  

.news-item p {  
  margin-top: 0px;  
  color: beige;
}  
</style>