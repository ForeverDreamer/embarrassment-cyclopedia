<template>
	<view>
		<view v-if="item.gstime" class="user-chat-time u-f-ajc">{{item.gstime}}</view>
		<view class="user-chat-list u-f" :class="{'user-chat-me': item.isme}">
			<image v-if="!item.isme" :src="item.userpic" mode="widthFix" lazy-load></image>
			
			<view class="user-chat-list-body">
				<!-- 文字 -->
				<text v-if="item.type==='text'">{{item.data}}</text>
				<!-- 图片 -->
				<image v-if="item.type==='img'" :src="item.data" mode="widthFix" lazy-load></image>
			</view>
			<image v-if="item.isme" :src="item.userpic" mode="widthFix" lazy-load></image>
		</view>
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
	.user-chat-list {
		padding: 20rpx 0;
	}
	.user-chat-list>image {
		width: 100rpx;
		height: 100rpx;
		border-radius: 100%;
		flex-shrink: 0;
	}
	.user-chat-list-body {
		position: relative;
		background: #F4F4F4;
		padding: 25rpx;
		margin-left: 20rpx;
		border-radius: 20rpx;
		margin-right: 100rpx;
	}
	.user-chat-list-body:after {
		position: absolute;
		left: -30rpx;
		top: 30rpx;
		right: 0;
		content: "";
		width: 0;
		height: 0;
		border: 16rpx solid #F4F4F4;
		border-color: transparent #F4F4F4 transparent transparent;
	}
	.user-chat-me {
		justify-content: flex-end;
	}
	.user-chat-me .user-chat-list-body {
		margin-right: 20rpx;
		margin-left: 100rpx;
	}
	.user-chat-me .user-chat-list-body:after {
		left: auto;
		right: -30rpx;
		border-color: transparent transparent transparent #F4F4F4;
	}
	.user-chat-list-body>image {
		max-width: 150rpx;
		max-height: 200rpx;
	}
	.user-chat-time {
		padding: 50rpx 0;
		color: #C7C7C7;
	}
</style>
