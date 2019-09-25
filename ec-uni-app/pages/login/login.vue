<template>
	<view>
		<!-- 状态栏 -->
		<uni-status-bar bgcolor="#FFE933"></uni-status-bar>
		<!-- 关闭按钮 -->
		<view class="icon iconfont icon-guanbi" @tap="back"></view>
		<!-- 引入背景图 -->
		<image class="loginhead" src="../../static/common/loginhead.png" mode="widthFix" lazy-load></image>
		<!-- 输入框+按钮 -->
		<view class="body">
			<!-- <input type="text" class="uni-input common-input" placeholder="昵称/手机号/邮箱" />
			<view class="login-input-box">
				<input type="text" class="uni-input common-input forget-input" placeholder="请输入密码" />
				<view class="forget u-f-ajc">忘记密码</view>
			</view> -->
			<view class="login-input-box">
				<view class="phone u-f-ajc">+86</view>
				<input type="text" class="uni-input common-input phone-input" placeholder="输入手机号码" />
			</view>
			<view class="login-input-box">
				<input type="text" class="uni-input common-input forget-input" placeholder="请输入验证码" />
				<view class="forget u-f-ajc">
					<view class="u-f-ajc yanzhengma login-font-color">获取验证码</view>
				</view>
			</view>
			<button class="user-set-btn" 
			:loading="loading" 
			:class="{'user-set-btn-disable':disabled}" 
			type="primary" @tap="submit" :disabled="disabled">完成
			</button>
		</view>
		<!-- 登录状态切换 -->
		<view class="login-status u-f-ajc login-padding login-font-color">
			验证码登录<view class="icon iconfont icon-jinru"></view>
		</view>
		<!-- 第三方登录 -->
		<view class="other-login-title u-f-ajc login-padding login-font-color">第三方登录</view>
		<other-login></other-login>
		<!-- 协议 -->
		<view class="login-rule u-f-ajc login-padding login-font-color">
			注册即代表您同意<view>《仿糗事百科用户协议》</view>
		</view>
	</view>
</template>

<script>
	import uniStatusBar from "../../components/uni-status-bar/uni-status-bar.vue";
	import otherLogin from "../../components/home/other-login.vue"
	
	export default {
		components: {
			uniStatusBar,
			otherLogin
		},
		data() {
			return {
				disabled: true,
				loading: false
			}
		},
		methods: {
			// 返回上一步
			back() {
				console.log("返回上一步");
			},
			// 提交登录
			submit() {
				console.log("提交登录");
			}
		}
	}
</script>

<style>
	@import "../../common/form.css";
	
	.login-font-color { color: #CCCCCC;}
	.login-padding { padding: 20rpx 0;}
	.icon-guanbi {
		position: fixed;
		top: 60rpx;
		left: 30rpx;
		font-size: 40rpx;
		font-weight: bold;
		color: #332F0A;
	}
	.loginhead {
		width: 100%;
	}
	.other-login-title {
		position: relative;
	}
	.other-login-title:before, .other-login-title:after {
		content: "";
		position: absolute;
		background: #CCCCCC;
		height: 1rpx;
		width: 100rpx;
		top: 50%;
	}
	.other-login-title:before {
		left: 25%;
	}
	.other-login-title:after {
		right: 25%;
	}
	.login-input-box {
		position: relative;
	}
	.login-input-box .forget-input {
		padding-right: 150rpx;
	}
	.login-input-box .forget, .login-input-box .phone {
		position: absolute;
		top: 0;
		height: 100%;
		z-index: 100;
	}
	.login-input-box .forget {
		right: 0;
		width: 150rpx;
	}
	.login-input-box .phone {
		left: 0;
		width: 100rpx;
		font-weight: bold;
	}
	.login-input-box .phone-input {
		padding-left: 110rpx;
	}
	.yanzhengma {
		background: #EEEEEE;
		border-radius: 10rpx;
		padding: 5rpx;
		width: 180rpx;
	}
</style>
