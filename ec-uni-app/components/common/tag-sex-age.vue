<template>
	<view class="tag-sex icon iconfont" :class="[sex==0?'icon-nan':'icon-nv']">
		{{age}}
	</view>
</template>

<script>
	export default {
		props: {
			sex: Number,
			age: Number
		}
	}
</script>

<style scoped>
	.tag-sex {
		background: #44B3FF;
		color: #FFFFFF;
		font-size: 23rpx;
		padding: 5rpx 10rpx;
		margin-left: 10rpx;
		border-radius: 20rpx;
		line-height: 22rpx;
	}
</style>
