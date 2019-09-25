<template>
	<view class="body">
		<uni-collapse>
			<uni-collapse-item v-for="(item, index) in list" :key="index" :title="item.title" :show-animation="true">
				<view style="padding: 30rpx;">
					{{item.content}}
				</view>
			</uni-collapse-item>
		</uni-collapse>
		<button class="user-set-btn" type="primary">意见反馈</button>
	</view>
</template>

<script>
	import uniCollapseItem from "../../components/uni-collapse-item/uni-collapse-item.vue";
	import uniCollapse from "../../components/uni-collapse/uni-collapse.vue";
	
	export default {
		components: {
			uniCollapseItem,
			uniCollapse
		},
		data() {
			return {
				list: [
					{
						title: "客服什么时候上线？",
						content: "123"
					},
					{
						title: "忘记账号/昵称/密码怎么办？",
						content: "456"
					},
					{
						title: "怎么搜索/查找/关注/取关用户？",
						content: "789"
					}
				]
			}
		},
		methods: {
			
		}
	}
</script>

<style>
	@import "../../common/form.css";
</style>
