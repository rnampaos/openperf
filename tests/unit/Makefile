#
# Makefile to build unit tests
#

all: tests

ICP_ROOT := $(realpath ../../)
ICP_TARGET := tests
include $(ICP_ROOT)/mk/bootstrap.mk

BUILD_DIR := $(ICP_BUILD_ROOT)/obj/unit
TARGET_DIR := $(ICP_BUILD_ROOT)/bin

SOURCES := \
	test_main.cpp \
	framework/test_init_factory.cpp \
	framework/test_list.cpp \
	framework/test_logging.cpp \
	framework/test_mac_address.cpp \
	framework/test_ipv4_address.cpp \
	framework/test_ipv4_network.cpp

OBJECTS := $(patsubst %, $(BUILD_DIR)/%, \
	$(patsubst %.cpp, %.o, $(SOURCES)))
SRC_DEPENDS := $(OBJECTS:.o=.d)

BLD_DEPENDS := catch framework

# Pull in dependencies
-include $(SRC_DEPENDS)
$(foreach DEP,$(BLD_DEPENDS),$(eval include $(ICP_ROOT)/mk/$(DEP).mk))

ICP_CONFIG_OPTS += --enable-static=yes --enable-shared=no
ICP_CPPFLAGS += $(addprefix -I,$(ICP_INC_DIRS))
ICP_LDFLAGS += $(addprefix -L,$(ICP_LIB_DIRS))

# Build rules
$(BUILD_DIR)/%.o: %.cpp | $(BLD_DEPENDS)
	@mkdir -p $(dir $@)
	$(strip $(ICP_CXX) -o $@ -c $(ICP_CPPFLAGS) $(ICP_CXXFLAGS) $(ICP_COPTS) $(ICP_DEFINES) $<)

$(TARGET_DIR)/test_inception: $(OBJECTS) $(BLD_DEPENDS)
	@mkdir -p $(dir $@)
	$(strip $(ICP_CXX) -o $@ $(ICP_LDOPTS) $(ICP_LDFLAGS) $(OBJECTS) $(ICP_LDLIBS))

.PHONY: tests
tests: $(TARGET_DIR)/test_inception
	$(TARGET_DIR)/test_inception

.PHONY: clean_tests
clean_tests:
	@rm -rf $(ICP_BUILD_ROOT)
clean: clean_tests