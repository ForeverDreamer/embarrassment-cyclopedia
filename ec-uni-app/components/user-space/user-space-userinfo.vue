<template>
	<view class="user-space-userinfo">
		<view class="user-space-userinfo-item">
			<view>账号信息</view>
			<view>糗龄: {{getRegAge}}</view>
			<view>糗百ID: {{userinfo.id}}</view>
		</view>
		<view class="user-space-userinfo-item">
			<view>个人信息</view>
			<view>星座: {{getXingZuo}}</view>
			<view>职业: {{userinfo.job}}</view>
			<view>故乡: {{userinfo.path}}</view>
			<view>情感状态: {{userinfo.qg}}</view>
		</view>
	</view>
</template>

<script>
	import t from "../../common/time.js";
	
	export default {
		props: {
			userinfo: Object
		},
		computed: {
			getRegAge() {
				return t.gettime.sumAge(this.userinfo.regtime);
			},
			getXingZuo() {
				return t.gettime.getHoroscope(this.userinfo.birthday);
			}
		}
	}
</script>

<style scoped>
	.user-space-userinfo {
		padding: 0 30rpx;
	}
	.user-space-userinfo-item {
		padding: 20rpx 0;
		border-bottom: 1rpx solid #EEEEEE;
	}
	.user-space-userinfo-item>view {
		color: #AAAAAA;
	}
	.user-space-userinfo-item>view:first-child {
		color: #333333;
		font-size: 35rpx;
		padding: 15rpx 0;
	}
</style>
