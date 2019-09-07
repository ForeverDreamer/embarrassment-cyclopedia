<template>
	<view>
		<view class="icon iconfont icon-changjingguanli animated fadeInDownBig" 
			  style="color: red; font-size: 100upx;">
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				title: '仿糗事百科'
			}
		},
		onLoad() {

		},
		methods: {

		}
	}
</script>

<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.logo {
		height: 200upx;
		width: 200upx;
		margin-top: 200upx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50upx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36upx;
		color: #8f8f94;
	}
</style>
