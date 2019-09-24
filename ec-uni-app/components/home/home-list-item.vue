<template>
	<view class="home-list-item u-f-ac u-f-jsb" hover-class="home-list-hover">
		<view class="u-f-ac">
			<view v-if="item.icon"
			class="icon iconfont"
			:class="['icon-'+item.icon]"></view>
			{{item.name}}
		</view>
		<view class="icon iconfont icon-jinru"></view>
	</view>
</template>

<script>
	export default {
		props: {
			item: Object,
			index: Number
		}
	}
</script>

<style scoped>
	.home-list {
		padding: 20rpx;
	}
	.home-list-item {
		border-top: 1rpx solid #F4F4F4;
		border-bottom: 1rpx solid #F4F4F4;
		padding: 20rpx;
	}
	.home-list-hover {
		background: #F4F4F4;
	}
	.home-list-item>view:first-child {
		color: #333333;
	}
	.home-list-item>view:first-child>view {
		margin-right: 10rpx;
	}
	.home-list-item>view:last-child {
		color: #CCCCCC;
	}
</style>
