<template>
	<view>
		<view class="paper-left-popup-mask" v-show="show" @tap="hidepopup"></view>
		<view class="paper-left-popup" v-show="show">
			<view class="u-f-ac" hover-class="paper-left-popup-h" @tap="addfriend">
				<view class="icon iconfont icon-sousuo"></view>
				<view>加糗友</view>
			</view>
			<view class="u-f-ac" hover-class="paper-left-popup-h" @tap="clear">
				<view class="icon iconfont icon-qingchu"></view>
				<view>清除未读</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		props: {
			show: Boolean
		},
		methods: {
			addfriend() {
				this.$emit('addfriend');
			},
			clear() {
				this.$emit('clear');
			},
			hidepopup() {
				this.$emit('hide');
			}
		}
	}
</script>

<style>
	.paper-left-popup-mask {
		position: fixed;
		right: 0;
		left: 0;
		top: 0;
		bottom: 0;
		z-index: 1999;
	}
	.paper-left-popup {
		position: fixed;
		right: 0;
		top: 100rpx;
		background: #FFFFFF;
		z-index: 2000;
		width: 55%;
		height: 180rpx;
		box-shadow: 1rpx 1rpx 20rpx 2rpx #CCCCCC;
	}
	.paper-left-popup>view {
		padding: 20rpx;
		font-size: 35rpx;
	}
	.paper-left-popup>view>view {
		margin-right: 10rpx;
		font-weight: bold;
	}
	.paper-left-popup-h {
		background: #EEEEEE;
	}
</style>
