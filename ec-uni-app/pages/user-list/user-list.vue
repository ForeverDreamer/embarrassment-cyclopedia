<template>
	<view>
		<!-- tabbar切换 -->
		<swiper-tab-head
		:tabBars="tabBars" 
		:tabIndex="tabIndex" 
		@tabtap="tabtap"
		scrollStyle="border-bottom: 0"
		scrollItemStyle="width: 33%">
		</swiper-tab-head>
	</view>
</template>

<script>
	import swiperTabHead from "../../components/index/swiper-tab-head.vue"

	export default {
		components: {
			swiperTabHead
		},
		data() {
			return {
				tabIndex: 0,
				tabBars: [
					{ name: "互关", id: "huguan", num: 10 },
					{ name: "关注", id: "guanzhu", num: 20 },
					{ name: "粉丝", id: "fensi", num: 30 },
				]
			}
		},
		// 监听导航按钮事件
		onNavigationBarButtonTap(e) {
			if (e.index==0) {
				uni.navigateBack({
					delta: 1
				});
			}
		},
		methods: {
			// tabbar点击事件
			tabtap(index) {
				this.tabIndex = index;
			}
		}
	}
</script>

<style>

</style>
