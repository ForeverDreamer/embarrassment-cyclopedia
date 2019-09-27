<template>
	<view class="user-space-head u-f-ajc">
		<!-- @tap.stop 阻止冒泡事件 -->
		<image :src="getBgImg" mode="widthFix" lazy-load @tap.stop="changeBgImg"></image>
		<view class="user-space-head-info u-f-ajc u-f-column">
			<image :src="userinfo.userpic" mode="widthFix" lazy-load></image>
			<view class="user-space-margin u-f-ac">
				{{userinfo.username}}
				<tag-sex-age :sex="userinfo.sex" :age="userinfo.age"></tag-sex-age>
			</view>
			<view class="icon iconfont user-space-head-btn user-space-margin"
			:class="[isguanzhu?'active':'icon-zengjia']"
			@tap.stop="guanzhu">
				{{isguanzhu?'已关注':'关注'}}
			</view>
		</view>
	</view>
</template>

<script>
	import tagSexAge from "../common/tag-sex-age.vue";
	
	export default {
		components: {
			tagSexAge
		},
		props: {
			userinfo: Object
		},
		data() {
			return {
				isguanzhu: this.userinfo.isguanzhu,
				bgimg: this.userinfo.bgimg
			}
		},
		computed: {
			getBgImg() {
				return "../../static/bgimg/" + this.bgimg + ".jpg";
			}
		},
		methods: {
			// 切换背景
			changeBgImg() {
				let num = parseInt(this.bgimg);
				this.bgimg = num = num<4 ? ++num : 1;
			},
			// 关注
			guanzhu() {
				this.isguanzhu = !this.userinfo.isguanzhu;
			}
		}
	}
</script>

<style scoped>
	.user-space-head {
		border: 1rpx solid;
		position: relative;
		height: 500rpx;
		overflow: hidden;
	}
	.user-space-head>image {
		width: 100%;
	}
	.user-space-head-info {
		position: absolute;
		top: 150rpx;
	}
	.user-space-head-info>image {
		width: 150rpx;
		height: 150rpx;
		border-radius: 100%;
	}
	.user-space-head-info>view:first-of-type {
		color: #FFFFFF;
		font-size: 35rpx;
		font-weight: bold;
		text-shadow: 2rpx 2rpx 10rpx #333333;
	}
	.user-space-head-btn {
		border: 1rpx solid #FFE933;
		background: #FFE933;
		color: #333333;
		padding: 0 5rpx;
		border-radius: 10rpx;
		font-size: 28rpx;
	}
	.active {
		background: none;
		color: #FFFFFF;
		border: 1rpx solid #FFFFFF;
	}
</style>
