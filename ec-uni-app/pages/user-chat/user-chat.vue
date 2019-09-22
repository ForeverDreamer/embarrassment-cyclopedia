<template>
	<view>
		<!-- 聊天列表 -->
		<view class="user-chat-list u-f user-chat-me">
			<!-- <image src="../../static/demo/userpic/11.jpg" mode="widthFix" lazy-load></image> -->
			
			<view class="user-chat-list-body">
				<!-- 文字 -->
				<!-- <text>当前输入的是当前输入的是当前输入的是当前输入的是当前输入的是当前输入的是</text> -->
				<!-- 图片 -->
				<image src="../../static/demo/3.jpg" mode="widthFix" lazy-load></image>
			</view>
			<image src="../../static/demo/userpic/11.jpg" mode="widthFix" lazy-load></image>
		</view>
		<!-- 输入框 -->
		<user-chat-bottom @submit="submit"></user-chat-bottom>
	</view>
</template>

<script>
	import userChatBottom from "../../components/user-chat/user-chat-bottom.vue"
	
	export default {
		components: {
			userChatBottom
		},
		data() {
			return {
				
			}
		},
		methods: {
			submit(data) {
				// 发送逻辑
				console.log("当前输入的是：" + data)
			}
		}
	}
</script>

<style>
	.user-chat-list {
		border: 1rpx solid;
	}
	.user-chat-list>image {
		width: 100rpx;
		height: 100rpx;
		border-radius: 100%;
		flex-shrink: 0;
	}
	.user-chat-list-body {
		border: 1rpx solid;
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
</style>
