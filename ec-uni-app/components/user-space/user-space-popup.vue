<template>
	<view>
		<view class="paper-left-popup-mask" v-show="show" @tap="hidepopup"></view>
		<view class="paper-left-popup" v-show="show">
			<view class="u-f-ac" hover-class="paper-left-popup-h" @tap="lahei">
				<view class="icon iconfont icon-sousuo"></view>
				<view>拉黑</view>
			</view>
			<view class="u-f-ac" hover-class="paper-left-popup-h" @tap="beizhu">
				<view class="icon iconfont icon-qingchu"></view>
				<view>备注</view>
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
			lahei() {
				this.$emit('lahei');
			},
			beizhu() {
				this.$emit('beizhu');
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
