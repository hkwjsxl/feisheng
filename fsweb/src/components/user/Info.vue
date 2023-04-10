<template>
  <div class="setting-right">
   <div class="setting-right-wrap wrap-boxes settings">
    <div class="formBox">
     <div id="setting-profile" class="setting-wrap setting-profile">
      <div class="common-title">
        个人信息
       <a href="javascript: void(0);" class="pull-right js-edit-info"><i class="el-icon-edit"></i>编辑</a>
      </div>
      <div class="line"></div>
      <div class="info-wapper">
       <div class="info-box clearfix">
        <label class="pull-left">昵称</label>
        <div class="pull-left">墨落</div>
       </div>
       <div class="info-box clearfix">
        <label class="pull-left">职位</label>
        <div class="pull-left">CG影视动画师</div>
       </div>
       <div class="info-box clearfix">
        <label class="pull-left">城市</label>
        <div class="pull-left">未设置</div>
       </div>
       <div class="info-box clearfix">
        <label class="pull-left">性别</label>
        <div class="pull-left">男</div>
       </div>
       <div class="info-box clearfix">
        <label class="pull-left">个性签名</label>
        <div class="pull-left">未设置</div>
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.clearfix:after {
	content: '\0020';
	display: block;
	height: 0;
	clear: both;
	visibility: hidden;
}

.setting-right {
	float: left;
	width: 1284px;
	box-sizing: border-box;
	background-color: #fff
}

.setting-right-wrap {
	min-height: 550px
}

.pull-left {
	float: left;
}

.pull-right {
	float: right;
}

.common-title {
	line-height: 32px;
	font-size: 16px;
	font-weight: 700;
}

.common-title a {
	color: #93999f;
	font-weight: 400;
}

.common-title a:hover {
	color: #008cc8;
}

.common-title a i {
	color: #008cc8;
	margin-right: 4px;
	vertical-align: middle;
}

.line {
	height: 1px;
	background-color: #d0d6d9;
	margin-top: 12px;
}

.setting-profile {
	padding: 0!important
}

.setting-profile .info-wapper {
	margin: 24px auto 24px 40px
}

.setting-profile .info-box {
	margin-bottom: 12px
}

.setting-profile .info-box label {
	width: 180px;
	line-height: 20px;
	padding: 20px 0;
	text-align: center;
	background-color: #f3f5f7;
	color: #07111b;
	font-weight: 700
}

.setting-profile .info-box div {
	width: 1034px;
	margin-left: 8px;
	line-height: 20px;
	padding: 20px 0 20px 22px;
	border-bottom: 1px solid #d9dde1
}

.edit-info .wlfg-wrap textarea {
	height: 70px
}

.edit-info .wlfg-wrap input {
	font-size: 14px
}

</style>